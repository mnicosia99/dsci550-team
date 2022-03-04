from lxml import etree
from lxml.html.soupparser import fromstring
from alive_progress import alive_bar

import argparse, json, re

import asm, plos_one

"""

Begin by adding additional features to the data about the author's lab size, affiliation, etc:

Required data (for all authors)
    Lab Size (number of students) - Approach is to scrape all articles with matching affiliation
    Publication Rate - Approach is to count total number of publications per author
    Other Journals Published In - Approach is to identify all journals the author was published in
    Information about First Author including
        Affiliation University
        Duration of Career (Years) - Approach is to calculatre based on timeframe author is publishing
        Highest degree obtained (e.g., “PhD”, “MS”)
        Degree Area (e.g., Computer Science)
        
Possible websites with data: 
    https://pubmed.ncbi.nlm.nih.gov/?term=Ying-Yi%20Chen%5BAuthor%5D&format=abstract&sort=jour&page=2
    https://www.ncbi.nlm.nih.gov/books/NBK25500/
    https://www.researchgate.net/profile/Ying-Yi-Chen
        lists publications
        Current institution
        Current position
        Location
        Dec 2018

"""

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

lab_size_map = dict()

def process_bik_dataset(lines):
    json_file = open('findings.json')
    findings_map = json.load(json_file)
    json_file.close()

    # for each row in the dataset, extract useful data and query url for additional data
    for position, line in enumerate(lines):
        if position == 0:
            continue
        authors_list = list()

        row_data = line.split("\t")
        authors_data = row_data[bik_dataset_column_headers['authors']].replace('and', '').replace('"', '').split(",")
        title = row_data[bik_dataset_column_headers['title']].strip()
        citation = row_data[bik_dataset_column_headers['citation']].strip()
        doi = row_data[bik_dataset_column_headers['doi']].strip()

        print("==============================DOI=====================================")
        print(doi)
        print("==============================Title=====================================")
        print(title)

        for a in authors_data:
            author = a.replace("&", "").strip()
            author = re.sub('\d', '', author)
            author = author.strip()
            if len(author) > 0:
                authors_list.append(author.strip())
            
        aff = get_affiliations(doi)

        # print("==============================Authors===================================")
        # for a in authors_list:
        #     author = a.strip()
        #     print(author)
            
        print("============================Affiliations for " + doi + "================================")
        for a in aff:
            affiliation = a.strip()
            print(affiliation)
        
        # if len(aff) > 0:
        findings_map[doi] = {"authors": authors_list, "affiliations" : aff}
        f = open("findings.json","w")
        json_string = json.dumps(findings_map)
        f.write(json_string)
        f.close()
        yield
            
    # print(findings_map)

    # json_string = json.dumps(findings_map)
    # f.write(json_string)

def get_bik_data(start, end):
    bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
    bf = open(bik_tsv_dataset_name, encoding="utf_8_sig")
    lines = list()
    
    if start > -1 and end > -1:
        lines = bf.readlines()[start: end]
    else:
        lines = bf.readlines()[0:]

    with alive_bar(len(lines) - 1) as bar:
        for i in process_bik_dataset(lines):
            bar()    

def process_affiliations(affiliations):
    json_file = open('labs.json')
    lab_size_map = json.load(json_file)
    json_file.close()
    
    for affiliation in affiliations:
        print(affiliation)
        lab_size = plos_one.get_lab_size(affiliation)
        lab_size_map[affiliation] = {"lab_size" : lab_size}
        print(lab_size_map[affiliation])
        yield

        json_string = json.dumps(lab_size_map)
        f = open("labs.json","w")
        f.write(json_string)
        f.close()

def process_authors(authors):
    json_file = open('authors.json')
    author_info_map = json.load(json_file)
    json_file.close()

    for author in authors:
        print(author)
        author_info = plos_one.get_labs_for_author(author)
        author_info_map[author] = {"author_info" : author_info}
        print(author_info_map[author])
        yield

        json_string = json.dumps(author_info_map)
        f = open("authors.json","w")
        f.write(json_string)
        f.close()

        
def get_author_data(start, end):
    # read the findings.json file to get authors and create a unique list
    authors = list()
    json_file = open('findings.json')
    finding_data = json.load(json_file)
    json_file.close()
    author_json_file = open('authors.json')
    author_data = json.load(author_json_file)
    author_json_file.close()
    for doi in finding_data:
        a_list = finding_data[doi]["authors"]
        for a in a_list:
            if not a in authors and not a in author_data:
                authors.append(a)
    
    # sort the list and get a slice between the provided range
    authors.sort()
    sliced_sorted_authors = authors[0:]
    if start > -1 and end > -1:
        sliced_sorted_authors = authors[start: end]
    
    # process_authors(authors)
    with alive_bar(len(sliced_sorted_authors)) as bar:
        for i in process_authors(sliced_sorted_authors):
            bar()    
                 
def get_affiliation_data(start, end):
    # read the findings.json file to get affiliations and create a unique list
    affiliations = list()
    json_file = open('findings.json')
    finding_data = json.load(json_file)
    json_file.close()
    labs_json_file = open('labs.json')
    lab_data = json.load(labs_json_file)
    labs_json_file.close()
    for doi in finding_data:
        a_list = finding_data[doi]["affiliations"]
        for a in a_list:
            if not a in affiliations and not a in lab_data:
                affiliations.append(a)
    
    print(len(affiliations))            
    # sort the list and get a slice between the provided range
    affiliations.sort()
    sliced_sorted_affiliations = affiliations[0:]
    if start > -1 and end > -1:
        sliced_sorted_affiliations = affiliations[start: end]
    
    with alive_bar(len(sliced_sorted_affiliations)) as bar:
        for i in process_affiliations(sliced_sorted_affiliations):
            bar()    
        
def get_affiliations(doi):
    aff = list()
    if doi.startswith("10.1371"):
        aff.extend(plos_one.get_affiliations(doi))
        pass
    elif doi.startswith("10.1128"): 
        l = asm.get_affiliations(doi)
        if l != None:
            aff.extend(l)
        pass
    elif doi.startswith("10.1155"):
        # aff.extend(hindawi.get_affiliations(doi))
        pass
    elif doi.startswith("10.1002"):
        # aff.extend(ijc.get_affiliations(doi))
        pass
    elif doi.startswith("10.1016"):
        # aff.extend(science_direct.get_affiliations(doi))
        pass
    return aff

if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add arguments
    parser.add_argument('--affiliations', action='store_true', default=False, help='A flag indicating that affiliations should be collected.')
    parser.add_argument('--author_data', action='store_true', default=False, help='A flag indicating that author data should be collected.')
    parser.add_argument('--bik_dataset', action='store_true', default=False, help='A flag indicating that data from the Bik dataset (tsv file) should be collected.')

    parser.add_argument('--bik_dataset_start', type=str)
    parser.add_argument('--bik_dataset_end', type=str)
    parser.add_argument('--author_data_start', type=str)
    parser.add_argument('--author_data_end', type=str)
    parser.add_argument('--affiliations_start', type=str)
    parser.add_argument('--affiliations_end', type=str)

    # Parse the arguments
    args = parser.parse_args()
    
    if args.bik_dataset:
        #  start at 0, end at n
        #  next start at n - 1 and end at 2n
        #  next start at 2n - 1 and end at 3n
        start = -1
        end = -1
        if args.bik_dataset_start and args.bik_dataset_end:
            start = args.bik_dataset_start
            end = args.bik_dataset_end
        get_bik_data(int(start), int(end))
    
    if args.affiliations:
        start = -1
        end = -1
        if args.affiliations_start and args.affiliations_end:
            start = args.affiliations_start
            end = args.affiliations_end
        get_affiliation_data(int(start), int(end))

    if args.author_data:
        start = -1
        end = -1
        if args.author_data_start and args.author_data_end:
            start = args.author_data_start
            end = args.author_data_end
        get_author_data(int(start), int(end))
    