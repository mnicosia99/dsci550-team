from requests_html import HTMLSession
from lxml.html.soupparser import fromstring
from lxml import etree
import urllib.parse

from page_load_util import load_article_page

resultsPerPage = 50
p = "&page=1"

# doi_org_url = "http://www.doi.org/"
affiliate_query_url = "https://journals.plos.org/plosone/search?resultsPerPage=" + str(resultsPerPage) + "&q=author_affiliate:"
author_query_url = "https://journals.plos.org/plosone/search?resultsPerPage=" + str(resultsPerPage) + "&q=author:"

# def load_article_page(doi):
#     # affiliationx contains map of affiliation to unique list of people, the len of list provides lab size
#     url = doi_org_url + doi
#     # print(url)   
#     root = None 
#     try:
#         session = HTMLSession()
#         page = session.get(url)
#         page.html.render(timeout=120)
#         root = fromstring(page.html.html) 
#         session.close()  
#     except:
#         print("Unable to load page: " + url)
#     return root

def load_articles_by_affiliate_page(affiliate):
    url = affiliate_query_url + "\"" + urllib.parse.quote(affiliate) + "\"" + p
    print(url)
    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=120)
    root = fromstring(r.html.html)            
    session.close()
    return root

def load_articles_by_author_page(author):
    url = author_query_url + "\"" + author + "\"" + p
    # print(url)
    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=120)
    root = fromstring(r.html.html)            
    session.close()
    return root

def get_affiliations(doi):
    affiliations = list()
    
    root = load_article_page(doi)
    if root == None:
        return affiliations
    author_list_items = root.xpath("//*[@id='author-list']/li")
    c = 0
    for author_list_item in author_list_items:
        # print(etree.tostring(author_list_item, pretty_print=True))
        author_names = author_list_item.xpath("//*[@data-author-id='" + str(c) + "']/text()")
        for author_name in author_names:
            if len(author_name.strip()) < 2:
                continue
            # print("========Author==========")
            # print(author_name.replace(",", "").strip())
            # print("========Affiliations==========")
            author_affiliations = author_list_item.xpath("//*[@id='authAffiliations-" + str(c) + "']/text()")
            for author_affiliation in author_affiliations:
                aa_split = author_affiliation.split(", \n")
                for aa in aa_split:
                    # print(aa.strip())
                    if not aa.strip() in affiliations:
                        affiliations.append(aa.strip())
        c += 1
    
    return affiliations

#  TODO this is no longer needed it seems
def get_author_count(doi, affiliate):
    affiliations = list()
    
    root = load_article_page(doi)
    if root == None:
        return affiliations
    author_list_items = root.xpath("//*[@id='author-list']/li")
    c = 0
    for author_list_item in author_list_items:
        # print(etree.tostring(author_list_item, pretty_print=True))
        author_names = author_list_item.xpath("//*[@data-author-id='" + str(c) + "']/text()")
        for author_name in author_names:
            if len(author_name.strip()) < 2:
                continue
            # print("========Author==========")
            # print(author_name.replace(",", "").strip())
            author_affiliations = author_list_item.xpath("//*[@id='authAffiliations-" + str(c) + "']/text()")
            for author_affiliation in author_affiliations:
                aa_split = author_affiliation.split(", \n")
                for aa in aa_split:
                    # print("========Affiliation==========")
                    # print(author_affiliation.strip())
                    if not aa.strip() in affiliations:
                        affiliations.append(aa.strip())
        c += 1
    
    return affiliations

def get_author_labs(root, author):
    labs = list()
    
    author_list_items = root.xpath("//*[@id='author-list']/li")
    c = 0
    for author_list_item in author_list_items:
        author_names = author_list_item.xpath("//*[@data-author-id='" + str(c) + "']/text()")
        for an in author_names:
            author_name = an.strip().replace(",", "")
            if author != author_name:
                continue
            print("========Author==========")
            print(author_name)
            author_affiliations = author_list_item.xpath("//*[@id='authAffiliations-" + str(c) + "']/text()")
            for author_affiliation in author_affiliations:
                aa_split = author_affiliation.split(", \n")
                for aa in aa_split:
                    print("========Affiliation==========")
                    print(aa.strip())
                    if not aa.strip() in labs:
                        labs.append(aa.strip())
        c += 1
    
    return labs

def get_affiliate_authors(root, affiliate):
    authors = list()
    author_list_items = root.xpath("//*[@id='author-list']/li")
    c = 0
    for author_list_item in author_list_items:
        # print(etree.tostring(author_list_item, pretty_print=True))
        author_names = author_list_item.xpath("//*[@data-author-id='" + str(c) + "']/text()")
        for an in author_names:
            author_name = an.strip().replace(",", "")
            if len(author_name) < 2:
                continue
            print("========Author==========")
            print(author_name)
            author_affiliations = author_list_item.xpath("//*[@id='authAffiliations-" + str(c) + "']/text()")
            for author_affiliation in author_affiliations:
                aa_split = author_affiliation.split(", \n")
                for aa in aa_split:
                    # print("========Affiliation==========")
                    # print(aa.strip())
                    if aa.strip() == affiliate and not author_name in authors:
                        authors.append(author_name)
                        # print("Adding author " + author_name)
        c += 1
    return authors

#  return lab size for a specific affiliate
def get_lab_size(affiliate):
    authors = list()
    root = load_articles_by_affiliate_page(affiliate)

    xpath_filter = ".//dt"            
    search_results = root.xpath(xpath_filter)    

    for search_result in search_results:
        data_doi = search_result.xpath("./@data-doi")[0]
        root = load_article_page(data_doi)
        if root == None:
            continue
        authors.extend(get_affiliate_authors(root, affiliate))
    return len(authors)

#  return labs for author
def get_labs_for_author(author):
    labs = list()
    journals = list()
    journal_names = list()
    first_pub_date = None
    last_pub_date = None
    author_info = dict()
    root = load_articles_by_author_page(author)

    xpath_filter = ".//dd"            
    search_results_1 = root.xpath(xpath_filter)   

    c = 0
    for search_result in search_results_1:
        # print(etree.tostring(search_result, pretty_print=True))
        journal_name = search_result.xpath("//*[@id='article-result-" + str(c) + "-journal-name']/text()")[0].strip()
        if not journal_name in journal_names:
            journal_names.append(journal_name)
        pub_date_data = search_result.xpath("//*[@id='article-result-" + str(c) + "-date']/text()")[0].strip().split(" ")
        pub_date = int(pub_date_data[len(pub_date_data) - 1])
        if first_pub_date == None or first_pub_date > pub_date:
            first_pub_date = pub_date
        if last_pub_date == None or last_pub_date < pub_date:
            last_pub_date = pub_date
        c += 1

    xpath_filter = ".//dt"            
    search_results_2 = root.xpath(xpath_filter)   
    
    for search_result in search_results_2:
        data_doi = search_result.xpath("./@data-doi")[0]
        journals.append(data_doi)
        root = load_article_page(data_doi)
        if root == None:
            continue
        labs.extend(get_author_labs(root, author))
    career_duration = "-1"
    if first_pub_date != None and last_pub_date != None:
        career_duration = last_pub_date - first_pub_date + 1
    author_info[author] = {"labs" : labs, "nbr_pubs": len(search_results_2), "published_journals": journal_names, "career_duration": career_duration, "first_pub_year" : first_pub_date, "last_pub_year" : last_pub_date}
    return author_info
