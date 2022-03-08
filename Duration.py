import requests
import json
from lxml import etree
from lxml.html.soupparser import fromstring

min_row = 0
max_row =216


affiliations = list()
findings = list()

# Organize Bik Data

bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
bf = open(bik_tsv_dataset_name, encoding="utf-8")

bik_dataset_column_headers = dict()
bik_dataset_column_headers['authors'] = 0
bik_dataset_column_headers['title'] = 1
bik_dataset_column_headers['citation'] = 2
bik_dataset_column_headers['doi'] = 3
bik_dataset_column_headers['year'] = 4
bik_dataset_column_headers['month'] = 5
bik_dataset_column_headers['dup'] = 6
bik_dataset_column_headers['dup_with_repos'] = 7
bik_dataset_column_headers['dup_with_alter'] = 8
bik_dataset_column_headers['cut_beautification'] = 9
bik_dataset_column_headers['findings'] = 10
bik_dataset_column_headers['reported'] = 11
bik_dataset_column_headers['correction_date'] = 12
bik_dataset_column_headers['retraction'] = 13
bik_dataset_column_headers['correction'] = 14
bik_dataset_column_headers['no_action'] = 15

# for each row in the dataset, extract useful data and query url for additional data
Career_Duration = []
for position, line in enumerate(bf):
    if (position) > min_row and (position) <= max_row:
        authors = list()
        affiliations = list()

        row_data = line.split("\t")
        authors_data = row_data[bik_dataset_column_headers['authors']].replace('and', '').replace('"', '').split(",")
        title = row_data[bik_dataset_column_headers['title']].strip()
        citation = row_data[bik_dataset_column_headers['citation']].strip()

        #Find paper in PubMed
        doi = row_data[bik_dataset_column_headers['doi']].strip().replace('�','-')
        if doi == '10.1016/S0169-5002(01)00212-4':
            url = 'https://pubmed.ncbi.nlm.nih.gov/11557119/'
        elif doi == '10.1016/S0169-5002(03)00239-3':
            url = 'https://pubmed.ncbi.nlm.nih.gov/12928127/'
        else:
            url = ('https://pubmed.ncbi.nlm.nih.gov/?term='+ doi).encode()

        page =  requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        xpath_filter = './/a[@class="full-name"]/@href'
        root = fromstring(page.text)
        nodes = root.xpath(xpath_filter)

        #Get years of publication and calculate Career Duration
        years = []
        url = 'https://pubmed.ncbi.nlm.nih.gov'+nodes[0]
        new_page = requests.get(url)
        new_xpath_filter = './/span[@class="docsum-journal-citation short-journal-citation"]/text()'
        new_root = fromstring(new_page.text)
        new_nodes = new_root.xpath(new_xpath_filter)
        for node in new_nodes:
            for word in node.replace(" ", "").split('.'):
               if word.isdigit():
                  years.append(int(word))

        Duration_Of_Career = max(years)-min(years)
        author_object = {}
        author_object[row_data[bik_dataset_column_headers['authors']]] = Duration_Of_Career
        Career_Duration.append(author_object)
        
#Write Data to JSON Document

out_file = open("Career_Duration.json", "w")

json.dump(Career_Duration, out_file, indent = 4)

out_file.close()
