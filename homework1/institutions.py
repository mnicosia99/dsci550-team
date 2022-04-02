# -*- coding: utf-8 -*-
"""institutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WN9dIRsVsyoVnwA5xdGOWUYjLkeCTPtR
"""

# Load in libraries
import pandas as pd
import json

# Import U.S. Department of Education data
df = pd.read_csv('MERGED2019_20_PP.csv')

# Select desired columns
universityData = df[["INSTNM", "LATITUDE", "LONGITUDE", "UGDS"]]
# Rename columns
universityData = universityData.rename(columns = {"INSTNM":'Institution', "LATITUDE":'Latitude', 
                                 "LONGITUDE":'Longitude', "UGDS":'UndergradStudentCount'})

# Change our dataframe to JSON
universityDataJSON = universityData.to_json(orient = 'records')
parsed = json.loads(universityDataJSON)

# Write to .json file
with open('universityData.json', 'w') as json_file:
 json.dump(universityDataJSON, json_file)