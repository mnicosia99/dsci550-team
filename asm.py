import asyncio
import pyppeteer
from requests_html import HTMLSession
from lxml.html.soupparser import fromstring
from lxml import etree
import urllib.parse
from bs4 import BeautifulSoup

from page_load_util import load_article_page

class HTMLSession2(HTMLSession):
    
    @property
    def browser(self):
        if not hasattr(self, "_browser"):
            self.loop = asyncio.get_event_loop()
            # self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=True, args=['--no-sandbox', '--proxy-server=pxu28134-0:aeu2T4Giav0dOiYg0lsz@x.botproxy.net:8080']))
            self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=False, args=['--no-sandbox']))
        return self._browser
    
def load_bs(doi, sleep_time = 1):
    doi_org_url = "http://www.doi.org/"
    # affiliationx contains map of affiliation to unique list of people, the len of list provides lab size
    url = doi_org_url + doi
    print(url)   
    root = None 
    try:
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36'}
        session = HTMLSession2()
        page = session.get(url)
        page.html.render(sleep=sleep_time, timeout=20)
        root = page.html.html
        session.close()  
    except:
        print("Unable to load page: " + url)
    return root

#  10.1128/IAI.69.10.6131Đ6139.2001
def get_affiliations(doi):
    affiliations = list()
    
    r = load_bs(doi + "#tab-contributors", 5)
    
    if r == None:
        print("Unable to load html")
        return
    # print(r)
    soup = BeautifulSoup(r, 'html.parser')
    results = soup.findAll("div", {"property" : "author"})
    print("=======================Results==========================")
    for result in results:
        family_names = result.findAll("span", {"property" : "familyName"})
        first_names = result.findAll("span", {"property" : "givenName"})
        affiliations_found = result.findAll("span", {"property" : "name"})
        name = ""
        if len(first_names) == 1:
            name += first_names[0].text.strip() + " "
        if len(family_names) == 1:
            name += family_names[0].text.strip()
        print("==================Author=====================")
        print(name)
        print("==================Affiliations=====================")
        for affiliation in affiliations_found:
            # a = affiliation.text
            print("==================Affiliation=====================")
            print(affiliation.text)
            affiliations.append(affiliation.text)
    print("==================Done with Results=====================")
    
    return affiliations
