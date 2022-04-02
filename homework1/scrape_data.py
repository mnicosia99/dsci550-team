from lxml import etree
from lxml.html.soupparser import fromstring
from alive_progress import alive_bar

import argparse, json, re
import asm, plos_one

"""
Generate additional features for the Bik et, al dataset 

Required data
    Lab Size (number of students):
        - Approach is to scrape all affiliations of each article and for each affiliation
          scrape all papers for the affiliated dept/university.  Using that information
          count how many authors are affiliated with the same dept/university.
    Publication Rate:
        - Approach is to scrape data for each author in each article and count total number 
          of publications for each author
    Other Journals Published In - Approach is to identify all journals the author was published in
        - Approach is to scrape data for each author in each article and identify all 
          publications for each author
    Affiliation University
        - Approach is to scrape all articles and for each author and identify each authors affiliation(s)
    Duration of Career (Years) 
        - Approach is to scrape data for each author and identify the start and end years that
          the author was publishing.  Subtract the start and end to get the numebr of years actively 
          publishing.
    Highest degree obtained (e.g., “PhD”, “MS”)
    Degree Area (e.g., Computer Science)
        
Possible websites to scrape data from are: 
    https://journals.plos.org/plosone
    https://pubmed.ncbi.nlm.nih.gov/?term=Ying-Yi%20Chen%5BAuthor%5D&format=abstract&sort=jour&page=2
    https://www.ncbi.nlm.nih.gov/books/NBK25500/
    https://www.researchgate.net/profile/Ying-Yi-Chen

"""

#  dictionary of the Bik et, al dataset columns to the humand readabler name of the column data
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

"""    
    For a row in the Bik et, al dataset retrieve data about the affiliations of the authors 
    attributed to the paper by scraping using lxml and xpath
"""
def process_bik_dataset(lines):
    #  Open the fidning.json file and read existing data
    json_file = open('findings.json')
    findings_map = json.load(json_file)
    json_file.close()

    # for each row in the Bik et, al dataset, extract useful data and query url for additional data
    for position, line in enumerate(lines):
        #  skip the first line in the Bik et, al dataset (the column headers)
        if position == 0:
            continue
        
        # List to collect the finding data for a specific paper (indexed by doi)
        authors_list = list()

        #  split the data for a single line in the Bik et, al dataset by the tab character
        row_data = line.split("\t")
        #  extract the various data from the line in the Bik et, al dataset
        authors_data = row_data[bik_dataset_column_headers['authors']].replace('and', '').replace('"', '').split(",")
        doi = row_data[bik_dataset_column_headers['doi']].strip()

        #  create list of authors from the Bik et, al dataset
        for a in authors_data:
            author = a.replace("&", "").strip()
            author = re.sub('\d', '', author)
            author = author.strip()
            if len(author) > 0:
                authors_list.append(author.strip())
          
        # get affiliations for the paper by doi  
        aff = get_affiliations(doi)

        # Create dictionary for the paper indexed by doi and containing 
        # the authors array and affiliations array
        findings_map[doi] = {"authors": authors_list, "affiliations" : aff}
        f = open("findings.json","w")
        json_string = json.dumps(findings_map)
        # Write the finding data to the json output file 
        f.write(json_string)
        f.close()
        yield
            
def get_bik_data(start, end):
    # Read the Bik et, al tsv file and process each line one at a time 
    bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
    bf = open(bik_tsv_dataset_name, encoding="utf_8_sig")
    lines = list()
    
    # This allows for processing a portion of the Bik et, al dataset
    if start > -1 and end > -1:
        lines = bf.readlines()[start: end]
    else:
        lines = bf.readlines()[0:]

    # Use the alive_progress library to provide a status indicator when running the data collection
    with alive_bar(len(lines) - 1) as bar:
        for i in process_bik_dataset(lines):
            bar()    

def process_affiliations(affiliations):
    json_file = open('labs.json')
    lab_size_map = json.load(json_file)
    json_file.close()
    
    for affiliation in affiliations:
        # Calculate data for a lab, number of students associated to the lab
        lab_size = plos_one.get_lab_size(affiliation)
        lab_size_map[affiliation] = {"lab_size" : lab_size}
        yield

        # Write the json file
        json_string = json.dumps(lab_size_map)
        f = open("labs.json","w")
        f.write(json_string)
        f.close()

def process_authors(authors):
    json_file = open('authors.json')
    author_info_map = json.load(json_file)
    json_file.close()

    for author in authors:
        # Calculate data for an author, number of publications and career duration
        author_info = plos_one.get_labs_for_author(author)
        author_info_map[author] = {"author_info" : author_info}
        yield

        # Write the json file
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
    # Read the existing author data
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
    
    # Use the alive_progress library to provide a status indicator when running the data collection
    with alive_bar(len(sliced_sorted_authors)) as bar:
        for i in process_authors(sliced_sorted_authors):
            bar()    
                 
def get_affiliation_data(start, end):
    # read the findings.json file to get affiliations and create a unique list
    affiliations = list()
    json_file = open('findings.json')
    finding_data = json.load(json_file)
    json_file.close()
    # Read the existing lab/affiliation data
    labs_json_file = open('labs.json')
    lab_data = json.load(labs_json_file)
    labs_json_file.close()
    # Process each lab to count the number of students associated to the lab to generate the lab size
    for doi in finding_data:
        a_list = finding_data[doi]["affiliations"]
        for a in a_list:
            if not a in affiliations and not a in lab_data:
                affiliations.append(a)
    
    # sort the list and get a slice between the provided range
    affiliations.sort()
    sliced_sorted_affiliations = affiliations[0:]
    if start > -1 and end > -1:
        sliced_sorted_affiliations = affiliations[start: end]
    
    # Use the alive_progress library to provide a status indicator when running the data collection
    with alive_bar(len(sliced_sorted_affiliations)) as bar:
        for i in process_affiliations(sliced_sorted_affiliations):
            bar()    

# Based on doi prefix scrape a different website that authorsed the paper
def get_affiliations(doi):
    aff = list()
    if doi.startswith("10.1371"):
        aff.extend(plos_one.get_affiliations(doi))
    elif doi.startswith("10.1128"): 
        l = asm.get_affiliations(doi)
        if l != None:
            aff.extend(l)
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

    # Process Bik et, al tsv file if this flag is present 
    if args.bik_dataset:
        #  default process the entire file indicated by -1 start and end
        start = -1
        end = -1
        if args.bik_dataset_start and args.bik_dataset_end:
            start = args.bik_dataset_start
            end = args.bik_dataset_end
        get_bik_data(int(start), int(end))
    
    # Generate the lab size data if this flag is present 
    if args.affiliations:
        start = -1
        end = -1
        if args.affiliations_start and args.affiliations_end:
            start = args.affiliations_start
            end = args.affiliations_end
        get_affiliation_data(int(start), int(end))

    # Generate the author number of publications and career duration if this flag is present 
    if args.author_data:
        start = -1
        end = -1
        if args.author_data_start and args.author_data_end:
            start = args.author_data_start
            end = args.author_data_end
        get_author_data(int(start), int(end))
    