#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import json
import requests

#get bik title and doi for search and joins
bik_dataset_column_headers = dict()
bik_dataset_column_headers['title'] = 1
bik_dataset_column_headers['doi'] = 3

bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
bf = open(bik_tsv_dataset_name, encoding="latin1")

# add bik data lines to dictionary
bik_data = {}
doi_list = []
title_list = []
index = 0
output = {}
for position, line in enumerate(bf):
    row_data = line.split("\t")
    title = row_data[bik_dataset_column_headers['title']].strip()
    doi = row_data[bik_dataset_column_headers['doi']].strip()
    
    if position > 0:
        bik_data[title] = doi
        doi_list.append(doi)
        title_list.append(title)

for title in title_list:
    curr_page = 'https://www.researchgate.net/search/publication?q='+title
    driver = webdriver.Chrome()
    # Make the driver wait 10 seconds
    driver.implicitly_wait(10)
    driver.get(curr_page)
    driver.implicitly_wait(10)
    #try to click the 1st author
    try:
        driver.find_element(By.CLASS_NAME, "nova-legacy-v-person-inline-item__fullname").find_element(By.XPATH, "./..").click()
        driver.implicitly_wait(10)
        try:
            #try to get the 1st author degree
            degree = driver.find_element(By.CSS_SELECTOR, '.nova-legacy-o-pack--vertical-align-bottom>.nova-legacy-o-pack__item').text
            driver.implicitly_wait(10)
            output[index] = {'title': title, 'doi': bik_data[title], 'degree': degree}
            index = index + 1
        except:
            pass
    except:
        pass
with open("degrees.json", "w") as outfile:
    json.dump(output, outfile)

