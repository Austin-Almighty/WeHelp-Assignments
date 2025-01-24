# Task 1
import csv
import json
import urllib.request
import re

#------Task 1.1
#URLs to the 2 webpages
page1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
page2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

#Load the pages as JSON files
with urllib.request.urlopen(page1) as response:
    data1 = json.load(response) 
with urllib.request.urlopen(page2) as response:
    data2 = json.load(response)

#extract the requested information from page 1 and save it to several lists
titles = [result['stitle'] for result in data1['data']['results']]
longitude = [result["longitude"] for result in data1['data']['results']]
latitude = [result['latitude'] for result in data1['data']['results']]
serial = [result['SERIAL_NO'] for result in data1['data']['results']] #Only used to match data in page2

url = [result['filelist'] for result in data1['data']['results']] #Long strings made up of several URLs
#Use regular expression to capture the first image URLs from the strings
image_url = []
pattern = r'https://.*?\.jpg'
for first in url:
    match = re.search(pattern, first, re.IGNORECASE) #capture both upper and lower cases file extension. i.e. .jpg/.JPG
    image_url.append(match.group())


#Create a dictionary of all the tourist destinations
destinations = [{"title":titles[i], "longitude":longitude[i], "latitude":latitude[i], "serial_no":serial[i], 'image_url':image_url[i]} for i in range(len(titles))]

# Add MRT stations and districts from the second JSON file to the dictionary
for location in destinations:
    for locale in data2['data']:
        if location['serial_no'] == locale['SERIAL_NO']: #Match the items from both files by checking for matching serial numbers
            location['MRT'] = locale['MRT']
            location['district'] = locale['address'][5:8]


#Write to spot.csv
with open('./week3/spot.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for spot in destinations:
        writer.writerow([spot['title'], spot['district'], spot['longitude'], spot['latitude'], spot['image_url']]) #Only output the required information


# ----Task 1.2
# A dictionary to group tourist destinations by nearest MRT stations
group_by_mrt = {}

for spot in destinations:
    station = spot['MRT']
    place = spot['title']
# If the current station is not in the dictionary, create a new list
    if station not in group_by_mrt:
        group_by_mrt[station] = []
    
    #add names of tourist attractions to the list
    group_by_mrt[station].append(place)
# group_by_mrt now: keys = names of MRT stations; values = [tourist attractions]


#Output the results to mrt.csv
with open('./week3/mrt.csv', mode='w', newline='', encoding='utf-8') as file2:
    writer = csv.writer(file2)
    for station, spots in group_by_mrt.items():
        row = [station] + spots #Add name of the station to the front of the list
        writer.writerow(row)

# Task 2
from bs4 import BeautifulSoup
#Starting URL of the PTT forum
landing_page = 'https://www.ptt.cc/bbs/Lottery/index.html'
base_url = "https://www.ptt.cc"

first_3_pages = [landing_page] #Initial a list that holds the URLs of the first three pages

# find url to next 2 pages
while len(first_3_pages) < 3:
    page = first_3_pages[-1]
    request = urllib.request.Request(page, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
})
    with urllib.request.urlopen(request) as response:
        data = response.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    a_tags = soup.find_all('a', class_='btn wide')
    next_page = ''
    for page in a_tags:
        if page.string == r'‹ 上頁':
            next_page = base_url+ page.get('href')
            first_3_pages.append(next_page)

#Obtain the links to articles from the first 3 pages
#Lists to hold the info we want
title_list = []
react_list = []
href_list = []
#Loop over the list of 3 pages
for page in first_3_pages:
    request = urllib.request.Request(page, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    })
    with urllib.request.urlopen(request) as response:
        data = response.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    # Scrap for <div> holding articles
    articles = soup.find_all('div', class_='r-ent')
    

    for article in articles:
        # Find the relevant tags
        title_div = article.find('div', class_='title')
        a_tag = title_div.find('a') if title_div else None  # Ensure title_div exists
        react_div = article.find('div', class_='nrec')
        span_tag = react_div.find('span') if react_div else None
        
        if a_tag:
            title_list.append(a_tag.string)
            href = a_tag.get('href')  
            href_list.append(href)
            if span_tag:
                react_list.append(span_tag.string)
            else:
                react_list.append('0')

# Links to all the articles
link_list = [base_url + href for href in href_list]
#List to hold the publish time
time_list = []
#Find the publish time from all articles
for link in link_list:
    request = urllib.request.Request(link, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    })
    with urllib.request.urlopen(request) as response:
        data = response.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
    
    outer_div = soup.find_all('div', class_='article-metaline')

    for middle in outer_div:
        tag = middle.find('span', class_='article-meta-tag')
        if tag.string == '時間':
            time = middle.find('span', class_='article-meta-value')
            time_list.append(time.text)
            break
    else:
        time_list.append('')
       
            
#Output the results to article.csv
with open('./week3/article.csv', mode='w', newline='', encoding='utf-8') as file3:
    writer = csv.writer(file3)
    for i in range(0, len(title_list)):
        row = [title_list[i], react_list[i], time_list[i]]
        writer.writerow(row)