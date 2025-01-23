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
with open('spot.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for spot in destinations:
        writer.writerow([spot['title'], spot['district'], spot['longitude'], spot['latitude'], spot['image_url']]) #Only output the required information


# ----Task 1.2


