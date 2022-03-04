#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import re
import requests
from bs4 import BeautifulSoup

#extract international city crime and safety statistics from numbeo
#numbeo license https://www.numbeo.com/common/terms_of_use.jsp
page = requests.get("https://www.numbeo.com/crime/rankings.jsp")
soup = BeautifulSoup(page.content, 'html.parser')
#list cities
citys = []
for each in soup.find_all('td', class_='cityOrCountryInIndicesTable'):
    citys.append(each.get_text())
#list statistics
crime_index = []
safety_index = []
x = 1
for each in soup.find_all('td', style='text-align: right'):
    if x == 1:
        crime_index.append(each.get_text())
    else:
        safety_index.append(each.get_text())
    x = (-1) * x
#combine city and statistics
output = {}
index = 0
key = '056266f45ea54187addfe95ee972201e'
for city in citys:
    #get geolocation for joining to University locations
    r = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+city+"&key="+key)
    lat = r.json()['results'][0]['geometry']['lat']
    lng = r.json()['results'][0]['geometry']['lng']
    #add all data to dictionary
    output[city] = {'crime_index': crime_index[index], 'safety_index': safety_index[index], 'city_crime_lat': lat, 'city_crime_lng': lng}
    index = index + 1

#export to .json file
with open("citycrimestats.json", "w") as outfile:
    json.dump(output, outfile)

