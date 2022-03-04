# -*- coding: utf-8 -*-
"""mergingData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ogb2IxoB2XZLvXG80nVrpr9vaLf7Q08J

Bik to CSV
"""
# Load in libraries
import pandas as pd
import requests
import json

# Read in Bik dataset
csvTable = pd.read_table('Bik_dataset-papers_with_endpoint_reached.tsv', sep = '\t', encoding = "ISO-8859-1")
# Select the rows with data and convert to a dataframe
df = pd.DataFrame(csvTable[0:214])

"""# Lab size"""
# Read in findings.json file
findingsData = pd.read_json('findings.json')

# Create empty labs list
labs = []

# Go through findings dataframe and append either the lab or a blank space
for col in findingsData:
  try:
    labs.append(findingsData[col][1][0])
  except:
    labs.append('')

# Set 'Labs' variable in our big dataframe to the filled labs list
df['Labs'] = labs

# Read in labs.json data
labsData = pd.read_json('labs.json')

# Go row by row through labsData. Join on df['Labs'] variable or leave a blank space
index = 0
labSizes = []
for index in range(len(df)):
  currentLab = df["Labs"][index]
  if currentLab != '':
    labSizes.append(labsData[currentLab][0])
  else:
    labSizes.append('')

# Set 'Lab Size' variable to our created list
df['Lab Size'] = labSizes

"""# Publication Rate"""
# Load in authors.json data
f = open('authors.json')
authorsData = json.load(f)

# Set nPublications to an empty list
nPublications = []

# set authors to be the 'Authors' in each row
index = 0
for index in range(len(df)):
  authors = df['Authors'][index]
#split the authors on commas
  splitAuthors = authors.split(", ")
  currentPubString = ''
  for author in splitAuthors:
    try:
        # create a string for each row containing the number of publications for corresponding authors. If none found then leave a blank
      currentPubString += str(authorsData[author]['author_info'][author]['nbr_pubs']) + ' '
    except:
      currentPubString += ' '
  # Append the string for each row into the nPublications list
  nPublications.append(currentPubString)
# Add the completed list as a 'nPublications' variable in the big dataframe
df['nPublications'] = nPublications

"""# Other Journals"""
# Create an empty list
otherJournals = []
# For each first author, find their 'published_journals' value in authorsData. Add those to the otherJournals list
index = 0
for index in range(len(df)):
  authors = df['Authors'][index]
  splitAuthors = authors.split(", ")
  currentJournalString = ''
  for author in splitAuthors:
    try:
      for i in range(len(authorsData[author]['author_info'][author]['published_journals'])):
        currentJournalString += authorsData[author]['author_info'][author]['published_journals'][i] + ' '
    except:
      currentJournalString += ' '
  otherJournals.append(currentJournalString)
# Add 'Other Journals' variable to the big dataframe
df["Other Journals"] = otherJournals

"""# University (first author)"""
# Bring in Affiliation.json data
f = open('Affiliation.json')
affiliationData = json.load(f)
# Create empty university list
university = []
# Append each university to the list
for i in range(len(affiliationData)):
  university.append(list(affiliationData[i].values())[0].strip())
# Set variable 'University' to the list
df['University'] = university

"""# Career Duration (first author)"""
# Load in Career_Duration.json
f = open('Career_Duration.json')
careerData = json.load(f)
# Set career lengths to an empty list
careerLengths = []
# Append career length data to the list
for i in range(len(careerData)):
  careerLengths.append(list(careerData[i].values())[0])
# Set 'Career Duration' variable to the careerLengths list
df['Career Duration'] = careerLengths

"""# Highest Degree Obtained (pending)

# Degree Area
"""
# Load Degree_Area.json
f = open('Degree_Area.json')
degreeData = json.load(f)
# Create blank list
degreeAreas = []
# Fill the list with the degree areas
for i in range(len(degreeData)):
  degreeAreas.append(list(degreeData[i].values())[0])
# Set 'Degree Area' variable to our list
df["Degree Area"] = degreeAreas

"""# Dataset 1"""
# Read in U.S. Department of Education Dataset
with open('universityData (2).json', encoding = 'utf-8') as inputfile:
  uniData = pd.read_json(inputfile)
# Rename Institution to University
uniData = uniData.rename(columns = {'Institution':'University'})
# Left join with our big dataframe on University
df = pd.merge(df, uniData, how = "left", on =["University", "University"])

"""# Dataset 2"""
# Read in university ranking data
with open('universities_ranking.json', encoding = 'utf-8') as inputfile:
  rankingData = pd.read_json(inputfile)
# Select our desired columns
rankingData = rankingData[['title', 'ranking', 'students staff ratio', 'perc intl students']]
# Rename title as University
rankingData = rankingData.rename(columns = {'title':'University'})
# Left join on University to our big dataframe
df = pd.merge(df, rankingData, how = "left", on=["University", "University"])

"""# Dataset 3"""

from math import sin, cos, sqrt, atan2, radians
key = ''#fa8ef19415fe4ffb8b9432730d61bcf8' --please minimize the use of this key
universities = list(df["University"])
uni_city = {}

with open('citycrimestats.json') as json_file:
    citydata = json.load(json_file)
cities = list(citydata.keys())
output = []

for university in universities:
    try:
        r = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+university+"&key="+key)
        lat = r.json()['results'][0]['geometry']['lat']
        lng = r.json()['results'][0]['geometry']['lng']
        best = 999999
        uni_city[university] = {'lat': lat, 'lng': lng}
        for city in cities:
            # approximate radius of earth in km to calculate nearst city/university
            R = 6373.0
            lat1 = radians(lat)
            lon1 = radians(lng)
            lat2 = radians(citydata[city]['city_crime_lat'])
            lon2 = radians(citydata[city]['city_crime_lng'])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            if distance < best:
                best_city = city
                best = distance
        output.append({'University': university, 'near_city': best_city, 'crime_index': citydata[best_city]['crime_index'], 
                         'safety_index': citydata[best_city]['safety_index']})
    
    except:
        output.append({'University': university})

citycrimestats = pd.DataFrame(output)

citycrimestats = citycrimestats[['University', 'near_city', 'crime_index', 'safety_index']]

df = pd.merge(df, citycrimestats, how = "left", on=["University", "University"])

#backup uni_city locations to reduce API use
with open("uni_locations.json", "w") as outfile:
    json.dump(uni_city, outfile)

# converting dataframe to tsv:
df.to_csv('merged_data.tsv', sep="\t")
