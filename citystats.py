import json
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
for city in citys:
    output[city] = {'crime_index': crime_index[index], 'safety_index': safety_index[index]}
    index = index + 1
#print(output)
with open("citystats.json", "w") as outfile:
    json.dump(output, outfile)