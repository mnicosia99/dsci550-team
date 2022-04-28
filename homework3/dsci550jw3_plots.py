# -*- coding: utf-8 -*-
"""dsci550jw3_plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hwIioe3J_QHoDY7m4tIqm__SHK0kq842
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""##NER Person"""

rawPerson = pd.read_csv('NCperson.csv')
totPerson = pd.read_csv('NEWperson.csv')

topPerson = pd.DataFrame(totPerson[0:24].drop(labels=[3, 13, 19, 20], axis=0))

plt.barh(topPerson['0'], topPerson['counts'], color='black')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned People in the News: March 2022')
plt.show()

rawPerson = pd.DataFrame(rawPerson)

topPeopleSource = rawPerson.loc[rawPerson['0'].isin(topPerson['0'])]

topCNNPeople = topPeopleSource.loc[topPeopleSource['Source'] == 'CNN']
plt.barh(topCNNPeople['0'], topCNNPeople['counts'], color='#CC0000')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned People by CNN: March 12-30, 2022')
plt.show()

topAljPeople = topPeopleSource.loc[topPeopleSource['Source'] == 'Alj']
plt.barh(topAljPeople['0'], topAljPeople['counts'], color='#d4a10f')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned People by Al Jazeera: March 12-30, 2022')
plt.show()

topFOXPeople = topPeopleSource.loc[topPeopleSource['Source'] == 'FOX']
plt.barh(topFOXPeople['0'], topFOXPeople['counts'], color='#003366')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned People by FOX News: March 12-30, 2022')
plt.show()

"""##NER ORG"""

rawORG = pd.read_csv('NCorg.csv')
totORG = pd.read_csv('NEWorg.csv')

topORG = pd.DataFrame(totORG[0:20])

plt.barh(topORG['0'], topORG['counts'], color='black')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Organizations in the News: March 2022')
plt.show()

rawORG = pd.DataFrame(rawORG)

topORGSource = rawORG.loc[rawORG['0'].isin(topORG['0'])]

topCNNORG = topORGSource.loc[topORGSource['Source'] == 'CNN']
plt.barh(topCNNORG['0'], topCNNORG['counts'], color='#CC0000')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Organizations by CNN: March 12-30, 2022')
plt.show()

topAljORG = topORGSource.loc[topORGSource['Source'] == 'Alj']
plt.barh(topAljORG['0'], topAljORG['counts'], color='#d4a10f')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Organizations by Al Jazeera: March 12-30, 2022')
plt.show()

topFOXORG = topORGSource.loc[topORGSource['Source'] == 'FOX']
plt.barh(topFOXORG['0'], topFOXORG['counts'], color='#003366')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Organizations by FOX News: March 12-30, 2022')
plt.show()

"""##Nationalities/Religious/Political Groups"""

rawNORP = pd.read_csv('NCnorp.csv')
totNORP = pd.read_csv('NEWnorp.csv')

topNORP = pd.DataFrame(totNORP[0:20])

plt.barh(topNORP['0'], topNORP['counts'], color='black')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Nationalities/Religious/Political Groups in the News: March 2022')
plt.show()

rawNORP = pd.DataFrame(rawNORP)

topNORPSource = rawNORP.loc[rawNORP['0'].isin(topNORP['0'])]

topCNNNORP = topNORPSource.loc[topNORPSource['Source'] == 'CNN']
plt.barh(topCNNNORP['0'], topCNNNORP['counts'], color='#CC0000')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Nationalities/Religious/Political Groups by CNN: March 12-30, 2022')
plt.show()

topAljNORP = topNORPSource.loc[topNORPSource['Source'] == 'Alj']
plt.barh(topAljNORP['0'], topAljNORP['counts'], color='#d4a10f')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Nationalities/Religious/Political Groups by Al Jazeera: March 12-30, 2022')
plt.show()

topFOXNORP = topNORPSource.loc[topNORPSource['Source'] == 'FOX']
plt.barh(topFOXNORP['0'], topFOXNORP['counts'], color='#003366')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Nationalities/Religious/Political Groups by FOX News: March 12-30, 2022')
plt.show()

"""##GPE: geo-political entities"""

rawGPE = pd.read_csv('NCgpe.csv')
totGPE = pd.read_csv('NEWgpe.csv')

topGPE = pd.DataFrame(totGPE[0:20])

plt.barh(topGPE['ID'], topGPE['Count'], color='black')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Geopolitical Entities in the News: March 2022')
plt.show()

rawGPE = pd.DataFrame(rawGPE)

topGPESource = rawGPE.loc[rawGPE['0'].isin(topGPE['ID'])]

topCNNGPE = topGPESource.loc[topGPESource['Source'] == 'CNN']
plt.barh(topCNNGPE['0'], topCNNGPE['counts'], color='#CC0000')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Geopolitical Entities by CNN: March 12-30, 2022')
plt.show()

topAljGPE = topGPESource.loc[topGPESource['Source'] == 'Alj']
plt.barh(topAljGPE['0'], topAljGPE['counts'], color='#d4a10f')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Geopolitical Entities by Al Jazeera: March 12-30, 2022')
plt.show()

topFOXGPE = topGPESource.loc[topGPESource['Source'] == 'FOX']
plt.barh(topFOXGPE['0'], topFOXGPE['counts'], color='#003366')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Geopolitical Entities by FOX News: March 12-30, 2022')
plt.show()

"""##LOC: Locations"""

rawLOC = pd.read_csv('NCloc.csv')
totLOC = pd.read_csv('NEWloc.csv')

topPerson = pd.DataFrame(totPerson[0:24].drop(labels=[3, 13, 19, 20], axis=0))

topLOC = pd.DataFrame(totLOC[0:23].drop(labels=[9, 14, 19]))

plt.barh(topLOC['ID'], topLOC['Count'], color='black')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Locations in the News: March 2022')
plt.show()

rawLOC = pd.DataFrame(rawLOC)

topLOCSource = rawLOC.loc[rawLOC['0'].isin(topLOC['ID'])]

topCNNLOC = topLOCSource.loc[topLOCSource['Source'] == 'CNN']
plt.barh(topCNNLOC['0'], topCNNLOC['counts'], color='#CC0000')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Locations by CNN: March 12-30, 2022')
plt.show()

topAljLOC = topLOCSource.loc[topLOCSource['Source'] == 'Alj']
plt.barh(topAljLOC['0'], topAljLOC['counts'], color='#d4a10f')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Locations by Al Jazeera: March 12-30, 2022')
plt.show()

topFOXLOC = topLOCSource.loc[topLOCSource['Source'] == 'FOX']
plt.barh(topFOXLOC['0'], topFOXLOC['counts'], color='#003366')
plt.xlabel('Count')
plt.title('Most Commonly Mentioned Locations by FOX News: March 12-30, 2022')
plt.show()