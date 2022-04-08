#!/usr/bin/env python
import os
import json
import requests
from lxml import etree
from lxml.html.soupparser import fromstring

min_row = 0
max_row =215

#Refer to the Bik Dataset for Metadata
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
count = 1
# for each row in the dataset, extract useful data and query url for additional data
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
            url = ('https://pubmed.ncbi.nlm.nih.gov/?term='+ doi)

        #Extract Metadata for each paper
        page =  requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        xpath_filter = './/div[@class="abstract-content selected"]/p/text()'
        reference_filter = './/li[@class="skip-numbering"]/text()'
        root = fromstring(page.text)
        nodes = root.xpath(xpath_filter)
        abstract = ''.join(nodes)
        reference = []
        references = root.xpath(reference_filter)
        for node in references:
            node = node.replace('-', '').replace('\u2013', '-').strip()
            if node != '':
                reference.append(node)
        author = []
        for a in authors_data:
            author.append(a.replace('\ufffd', '-').strip())

        #Save Metadata into a JSON to combine with extracted text
        grover = {'summary': abstract.strip().replace('\n', ' ').replace('\t', ' '),
            'title': title.replace('"',''),
            'text': '',
            'references': reference,
            'authors': author,
            'publish_date': '12-22-2011',
            'iso_date': '12-22-2011',
            'domain': "researchgate.com",
            'image_url': '',
            'tags': []}
        try:
            out_file = open("Metadata/Article"+str(count)+".json", "w")
            json.dump(grover, out_file, indent = 4)
            out_file.close()
            count += 1
        except:
            continue


#Combine Metadata with Tika Extracted text to get JSONs for Grover Input
for file in os.listdir('Extracted_Text'):
    for file2 in os.listdir('Metadata'):
        f1 = open('Extracted_Text/'+file)
        if file.endswith('.json'):
            content = json.load(f1)
        if file2.endswith('.json'):
            f2 = open('Metadata/'+file2)
            meta = json.load(f2)
            if meta["title"][:10] in content['text']:
                meta["text"] = content["text"].strip()
                out_file = open("Grover_Input/" + file, "w")
                json.dump(meta, out_file, indent=4)
                out_file.close()
