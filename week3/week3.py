import csv
import json
import urllib.request

#URLs to the 2 webpages
page1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
page2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

#Load the pages as JSON files
with urllib.request.urlopen(page1) as response:
    data1 = json.load(response) 
with urllib.request.urlopen(page2) as response:
    data2 = json.load(response)

#extract the requested information from page 1 and save it to several lists
locations = [result['stitle'] for result in data1['data']['results']]
longitude = [result["longitude"] for result in data1['data']['results']]
latitude = [result['latitude'] for result in data1['data']['results']]

serial = [result['SERIAL_NO'] for result in data1['data']['results']] #Only used to match data in page2
