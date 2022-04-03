import json
import requests
import os
import glob
import time
import researchGate_id

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

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
        bik_data[doi] = title
        doi_list.append(doi)
        title_list.append(title)

doi_not_found = {}

#identify the path to the downloaded files
home = os.path.expanduser("~")
downloadspath=os.path.join(home, "Downloads")
list_of_files = glob.glob(downloadspath+"\*.pdf")
i = 0
file_locations = {}

def add_filename(doi):
    time.sleep(2)
    home = os.path.expanduser("~")
    downloadspath=os.path.join(home, "Downloads")
    list_of_files = glob.glob(downloadspath+"\*.pdf")
    latest_file = max(list_of_files, key=os.path.getctime)
    fname = ''
    for letter in latest_file:
        if letter =='\\':
            fname = ''
        else:
            fname = fname+letter
    file_locations[doi] = fname

doi_not_found = {}

#check wiley.com for DOI downloads while avoiding the cloud flare bot blocker with undetected_chromedriver
driver = uc.Chrome()
wiley_not_found_doi = []

for doi in doi_list:
    try:
        # Make the driver wait 10 seconds when needed
        driver.implicitly_wait(10)
        #get wiley PDFs
        driver.get("https://onlinelibrary.wiley.com/doi/pdfdirect/"+doi+"?download=true")
        driver.implicitly_wait(10)
        try:
            #save doi to a list if it didn't download by checking for any 'sub' class name
            driver.find_element(By.CLASS_NAME, "sub")
            wiley_not_found_doi.append(doi)
        except:
            add_filename(doi)
    except:
        pass

#try Research Gate for the missing DOI's
username = researchGate_id.user
password = researchGate_id.password

driver.implicitly_wait(10)
# Log into an account
# Log in page
driver.get("https://www.researchgate.net/login")
# Type the user and password
driver.find_element(By.ID, "input-login").send_keys(username)
driver.find_element(By.ID, "input-password").send_keys(password)
# Actually log in
driver.find_element(By.CLASS_NAME, "nova-legacy-c-button__label").find_element(By.XPATH, "./..").click()

rg_not_found_doi = []
    
for doi in wiley_not_found_doi:
    #try to click the download button the article
    try:
        curr_page = 'https://www.researchgate.net/search/publication?q='+doi
        #Make the driver wait 10 seconds
        driver.implicitly_wait(10)
        driver.get(curr_page)
        #driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.LINK_TEXT, "Download").click()
        driver.implicitly_wait(10)
        add_filename(doi)
    except:
        try:
            #find the article by "title" if doi not found
            url = 'https://www.researchgate.net/search/publication?q=%22'+bik_data[doi]+'%22'
            driver.implicitly_wait(10)
            driver.get(url)
            driver.implicitly_wait(10)
            driver.find_element(By.LINK_TEXT, "Download").click()
            driver.implicitly_wait(10)
            add_filename(doi)
        except:
            rg_not_found_doi.append(doi)

missed_doi = {}
index = 0

#change settings to make the pdf immediatelly download instead of opening in browser and asking to rename
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome(options=options)

#Cycle through the remaining DOI's in the USC Library
for doi in rg_not_found_doi:
    try:
        url = 'https://uosc.primo.exlibrisgroup.com/discovery/search?query=any,contains,%22'+doi+'%22&tab=Everything&search_scope=MyInst_and_CI&vid=01USC_INST:01USC&lang=en&offset=0'
        driver.implicitly_wait(10)
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(By.CLASS_NAME, "browzine-direct-to-pdf-link").find_element(By.XPATH, "./..").click()
        driver.implicitly_wait(10)
        add_filename(doi)
    except:
        try:
            #check by name when the given doi isn't a match
            url = 'https://uosc.primo.exlibrisgroup.com/discovery/search?query=any,contains,%22'+bik_data[doi]+'%22&tab=Everything&search_scope=MyInst_and_CI&vid=01USC_INST:01USC&lang=en&offset=0'
            driver.implicitly_wait(10)
            driver.get(url)
            driver.implicitly_wait(10)
            driver.find_element(By.CLASS_NAME, "browzine-direct-to-pdf-link").find_element(By.XPATH, "./..").click()
            driver.implicitly_wait(10)
            add_filename(doi)
        except:
            #try one more time with extra sleep time
            try:
                time.sleep(10)
                url = 'https://uosc.primo.exlibrisgroup.com/discovery/search?query=any,contains,%22'+doi+'%22&tab=Everything&search_scope=MyInst_and_CI&vid=01USC_INST:01USC&lang=en&offset=0'
                driver.implicitly_wait(10)
                driver.get(url)
                driver.implicitly_wait(10)
                time.sleep(10)
                driver.find_element(By.CLASS_NAME, "browzine-direct-to-pdf-link").find_element(By.XPATH, "./..").click()
                driver.implicitly_wait(10)
                add_filename(doi)
            except:
                missed_doi[index] = doi
                index = index + 1


#save missing items to .json
with open("missed_doi.json", "w") as outfile:
    json.dump(missed_doi, outfile)
    
#save file names to .json
with open("file_locations.json", "w") as outfile:
    json.dump(file_locations, outfile)
