# -*- coding: utf-8 -*-
"""hw3groupingNER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18fjos-nKTVvyifTpVKvCqup_uFC8QPz5
"""

import json
import pandas as pd

"""Load in 31 CNN files"""

numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09']

for i in range(10,32):
  numbers.append(str(i))

numbers

CNNperson=[]
CNNnorp=[]
CNNorg=[]
CNNgpe=[]
CNNloc=[]

for i in range(len(numbers)):
  f = open('/content/drive/MyDrive/DSCI 550/cnn_NER_tokenization/' + numbers[i] + '/tokenized_' + numbers[i] +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      CNNperson.append(key)

    elif val=='NORP':
      CNNnorp.append(key)

    elif val=='ORG':
      CNNorg.append(key)

    elif val=='GPE':
      CNNgpe.append(key)

    elif val=='LOC':
      CNNloc.append(key)

CNNpersonCounts = pd.DataFrame(CNNperson)
CNNnorpCounts = pd.DataFrame(CNNnorp)
CNNorgCounts = pd.DataFrame(CNNorg)
CNNgpeCounts = pd.DataFrame(CNNgpe)
CNNlocCounts = pd.DataFrame(CNNloc)
CNNpersonCounts = CNNpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNnorpCounts = CNNnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNorgCounts = CNNorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNgpeCounts = CNNgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNlocCounts = CNNlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNpersonCounts['Source'] = 'CNN'
CNNnorpCounts['Source'] = 'CNN'
CNNorgCounts['Source'] = 'CNN'
CNNgpeCounts['Source'] = 'CNN'
CNNlocCounts['Source'] = 'CNN'

"""### Aljazeera

Load in 31 Aljazeera files
"""

Aljperson=[]
Aljnorp=[]
Aljorg=[]
Aljgpe=[]
Aljloc=[]

for i in range(len(numbers[:-1])):
  f = open('/content/drive/MyDrive/DSCI 550/aljazeera_NER_tokenization/' + numbers[i] + '/tokenized_' + numbers[i] +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      Aljperson.append(key)

    elif val=='NORP':
      Aljnorp.append(key)

    elif val=='ORG':
      Aljorg.append(key)

    elif val=='GPE':
      Aljgpe.append(key)

    elif val=='LOC':
      Aljloc.append(key)



AljpersonCounts = pd.DataFrame(Aljperson)
AljnorpCounts = pd.DataFrame(Aljnorp)
AljorgCounts = pd.DataFrame(Aljorg)
AljgpeCounts = pd.DataFrame(Aljgpe)
AljlocCounts = pd.DataFrame(Aljloc)
AljpersonCounts = AljpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljnorpCounts = AljnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljorgCounts = AljorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljgpeCounts = AljgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljlocCounts = AljlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljpersonCounts['Source'] = 'Alj'
AljnorpCounts['Source'] = 'Alj'
AljorgCounts['Source'] = 'Alj'
AljgpeCounts['Source'] = 'Alj'
AljlocCounts['Source'] = 'Alj'



"""###FOX"""

FOXperson=[]
FOXnorp=[]
FOXorg=[]
FOXgpe=[]
FOXloc=[]

for i in range(12,32):
  f = open('/content/drive/MyDrive/DSCI 550/fox_NER_tokenization/' + str(i) + '/tokenized_' + str(i) +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      FOXperson.append(key)

    elif val=='NORP':
      FOXnorp.append(key)

    elif val=='ORG':
      FOXorg.append(key)

    elif val=='GPE':
      FOXgpe.append(key)

    elif val=='LOC':
      FOXloc.append(key)



FOXpersonCounts = pd.DataFrame(FOXperson)
FOXnorpCounts = pd.DataFrame(FOXnorp)
FOXorgCounts = pd.DataFrame(FOXorg)
FOXgpeCounts = pd.DataFrame(FOXgpe)
FOXlocCounts = pd.DataFrame(FOXloc)
FOXpersonCounts = FOXpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXnorpCounts = FOXnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXorgCounts = FOXorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXgpeCounts = FOXgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXlocCounts = FOXlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXpersonCounts['Source'] = 'FOX'
FOXnorpCounts['Source'] = 'FOX'
FOXorgCounts['Source'] = 'FOX'
FOXgpeCounts['Source'] = 'FOX'
FOXlocCounts['Source'] = 'FOX'



type(FOXpersonCounts)

"""####JOIN and Count"""



totalPerson = pd.concat([CNNpersonCounts, AljpersonCounts, FOXpersonCounts])
totalNORP = pd.concat([CNNnorpCounts, AljnorpCounts, FOXnorpCounts])
totalORG = pd.concat([CNNorgCounts, AljorgCounts, FOXorgCounts])
totalGPE = pd.concat([CNNgpeCounts, AljgpeCounts, FOXgpeCounts])
totalLOC = pd.concat([CNNlocCounts, AljlocCounts, FOXlocCounts])
totalPerson.to_csv('NERperson.csv', index=False)
totalNORP.to_csv('NERnorp.csv', index=False)
totalORG.to_csv('NERorg.csv', index=False)
totalGPE.to_csv('NERgpe.csv', index=False)
totalLOC.to_csv('NERloc.csv', index=False)

"""### Get source distribuitions"""

for i in range(12,31):
  print(i)

CNNperson=[]
CNNnorp=[]
CNNorg=[]
CNNgpe=[]
CNNloc=[]

for i in range(12,31):
  f = open('/content/drive/MyDrive/DSCI 550/cnn_NER_tokenization/' + str(i) + '/tokenized_' + str(i) +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      CNNperson.append(key)

    elif val=='NORP':
      CNNnorp.append(key)

    elif val=='ORG':
      CNNorg.append(key)

    elif val=='GPE':
      CNNgpe.append(key)

    elif val=='LOC':
      CNNloc.append(key)

CNNpersonCounts = pd.DataFrame(CNNperson)
CNNnorpCounts = pd.DataFrame(CNNnorp)
CNNorgCounts = pd.DataFrame(CNNorg)
CNNgpeCounts = pd.DataFrame(CNNgpe)
CNNlocCounts = pd.DataFrame(CNNloc)
CNNpersonCounts = CNNpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNnorpCounts = CNNnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNorgCounts = CNNorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNgpeCounts = CNNgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNlocCounts = CNNlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
CNNpersonCounts['Source'] = 'CNN'
CNNnorpCounts['Source'] = 'CNN'
CNNorgCounts['Source'] = 'CNN'
CNNgpeCounts['Source'] = 'CNN'
CNNlocCounts['Source'] = 'CNN'

Aljperson=[]
Aljnorp=[]
Aljorg=[]
Aljgpe=[]
Aljloc=[]

for i in range(12,31):
  f = open('/content/drive/MyDrive/DSCI 550/aljazeera_NER_tokenization/' + str(i) + '/tokenized_' + str(i) +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      Aljperson.append(key)

    elif val=='NORP':
      Aljnorp.append(key)

    elif val=='ORG':
      Aljorg.append(key)

    elif val=='GPE':
      Aljgpe.append(key)

    elif val=='LOC':
      Aljloc.append(key)

AljpersonCounts = pd.DataFrame(Aljperson)
AljnorpCounts = pd.DataFrame(Aljnorp)
AljorgCounts = pd.DataFrame(Aljorg)
AljgpeCounts = pd.DataFrame(Aljgpe)
AljlocCounts = pd.DataFrame(Aljloc)
AljpersonCounts = AljpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljnorpCounts = AljnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljorgCounts = AljorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljgpeCounts = AljgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljlocCounts = AljlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
AljpersonCounts['Source'] = 'Alj'
AljnorpCounts['Source'] = 'Alj'
AljorgCounts['Source'] = 'Alj'
AljgpeCounts['Source'] = 'Alj'
AljlocCounts['Source'] = 'Alj'

FOXperson=[]
FOXnorp=[]
FOXorg=[]
FOXgpe=[]
FOXloc=[]

for i in range(12,31):
  f = open('/content/drive/MyDrive/DSCI 550/fox_NER_tokenization/' + str(i) + '/tokenized_' + str(i) +'.json')
  data = json.load(f)
  for key, val in data.items():

    if val=='PERSON':
      FOXperson.append(key)

    elif val=='NORP':
      FOXnorp.append(key)

    elif val=='ORG':
      FOXorg.append(key)

    elif val=='GPE':
      FOXgpe.append(key)

    elif val=='LOC':
      FOXloc.append(key)

FOXpersonCounts = pd.DataFrame(FOXperson)
FOXnorpCounts = pd.DataFrame(FOXnorp)
FOXorgCounts = pd.DataFrame(FOXorg)
FOXgpeCounts = pd.DataFrame(FOXgpe)
FOXlocCounts = pd.DataFrame(FOXloc)
FOXpersonCounts = FOXpersonCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXnorpCounts = FOXnorpCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXorgCounts = FOXorgCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXgpeCounts = FOXgpeCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXlocCounts = FOXlocCounts.groupby([0]).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
FOXpersonCounts['Source'] = 'FOX'
FOXnorpCounts['Source'] = 'FOX'
FOXorgCounts['Source'] = 'FOX'
FOXgpeCounts['Source'] = 'FOX'
FOXlocCounts['Source'] = 'FOX'

totalPerson = pd.concat([CNNpersonCounts, AljpersonCounts, FOXpersonCounts])
totalNORP = pd.concat([CNNnorpCounts, AljnorpCounts, FOXnorpCounts])
totalORG = pd.concat([CNNorgCounts, AljorgCounts, FOXorgCounts])
totalGPE = pd.concat([CNNgpeCounts, AljgpeCounts, FOXgpeCounts])
totalLOC = pd.concat([CNNlocCounts, AljlocCounts, FOXlocCounts])
totalPerson.to_csv('CorrectDaysperson.csv', index=False)
totalNORP.to_csv('CorrectDaysnorp.csv', index=False)
totalORG.to_csv('CorrectDaysorg.csv', index=False)
totalGPE.to_csv('CorrectDaysgpe.csv', index=False)
totalLOC.to_csv('CorrectDaysloc.csv', index=False)