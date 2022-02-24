from lxml import etree
from lxml.html.soupparser import fromstring

import requests
from finding import Finding
from author import Author

"""

Begin by adding additional features to the data about the author’s lab size, affiliation, etc:

https://www.researchgate.net/profile/Ying-Yi-Chen
    lists publications
    Current institution
    Current position
    Location
    Dec 2018

    a. Lab Size (number of students)
    b. Publication Rate
    c. Other Journals Published In
    d. Information about First Author including
        i. Affiliation University
        ii. Duration of Career (Years)
        iii. Highest degree obtained (e.g., “PhD”, “MS”)
        iv. Degree Area” (e.g., Computer Science)  
      
    https://pubmed.ncbi.nlm.nih.gov/?term=Ying-Yi%20Chen%5BAuthor%5D&format=abstract&sort=jour&page=2
    https://www.ncbi.nlm.nih.gov/books/NBK25500/

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

doi_org_url = "http://www.doi.org/"

min_row = 101
max_row = 150

affiliations = list()
findings = list()

bik_tsv_dataset_name = "Bik_dataset-papers_with_endpoint_reached.tsv"
bf = open(bik_tsv_dataset_name, encoding="latin1")

# for each row in the dataset, extract useful data and query url for additional data
for position, line in enumerate(bf):
    if position >= min_row and position <= max_row:    
        authors = list()
        affiliations = list()

        row_data = line.split("\t")
        authors_data = row_data[bik_dataset_column_headers['authors']].replace('and', '').replace('"', '').split(",")
        title = row_data[bik_dataset_column_headers['title']].strip()
        citation = row_data[bik_dataset_column_headers['citation']].strip()
        doi = row_data[bik_dataset_column_headers['doi']].strip()

        print("=======================================================")
        print(position)
        print(title)
        for author in authors_data:
            authors.append(author.strip())
            
        if '10.1155'in doi:
            url = doi_org_url + doi
            print(url)
            page = requests.get(url)
            xpath_filter = ".//*[contains(@class, 'article_authors')]"            
            root = fromstring(page.text)            
            nodes = root.xpath(xpath_filter)

            for node in nodes:
                # spans are authors (text or text in b, sup is reference ro ref_info below
                spans = node.xpath("./span")
                for span in spans:
                    author = span.xpath("./text()|./b/text()")
                    print(author[0])
                # div is Affiliations (sup, span)
                paragraphs = node.xpath("./div/p")
                for p in paragraphs:
                    # print(etree.tostring(p, pretty_print=True))
                    ref_info = p.xpath("./span/text()")
                    print(ref_info)
        elif '10.1002' in doi:
            url = doi_org_url + doi
            print(url)
            page = requests.get(url)
            xpath_filter = ".//*[contains(@class, 'article_authors')]"   
            xpath_filter = ".//*[contains(@class, 'hidden-xs') and contains(@class, 'desktop-authors')]"         
            xpath_filter = ".//*[contains(@class, 'hidden-xs')]"         
            root = fromstring(page.text)
            # div with classes loa-wrapper loa-authors hidden-xs desktop-authors  
            divs = root.xpath(xpath_filter)
            for div in divs:
                print(etree.tostring(div, pretty_print=True))                
                #  contains array of spans with classes accordion__closed accordion-tabbed__tab
                spans = div[0].xpath("//span/*[contains(@class, 'accordion__closed accordion-tabbed__tab')]")
                for span in spans:
                    # div which has p (class author_name, name is in text) and p with ref_info in text
                    author_div = span.xpath("//div/*[contains(@class, 'author-info accordion-tabbed__content')]")[0]
                    author_name = author_div.xpath("//p/*[contains(@class, 'author-name')]")[0]
                    print(author_name)
                    ref_info = author_div.xpath("//p[not(@*)/text()")
                    print(ref_info)
            
        elif '10.1371' in doi:
            url = doi_org_url + doi
            page = requests.get(url)        

            # for r in res:
            #     span = r.select("span")
            #     for s in span:
            #         if s.text == "Affiliation":
            #             for c in r.children:
            #                 if isinstance(c, bs4.element.NavigableString):
            #                     if not c.strip() in affiliations:
            #                         affiliations.append(c.strip())
        
        finding = {
            "author": authors, 
            "title": title,
            "citation": citation,
            "doi": doi,
            "affiliation" : affiliations
        }
        findings.append(finding)
