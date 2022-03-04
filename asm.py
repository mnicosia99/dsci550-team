import asyncio
import pyppeteer
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#  Class to override the browser function so it does not run headless
# headless=False was required to get the javascript to render properly
class HTMLSession2(HTMLSession):
    
    @property
    def browser(self):
        if not hasattr(self, "_browser"):
            self.loop = asyncio.get_event_loop()
            self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=False, args=['--no-sandbox']))
        return self._browser

# Load the data using the overridden HTMLSession (non-headless) 
def load_bs(doi, sleep_time = 1):
    doi_org_url = "http://www.doi.org/"
    url = doi_org_url + doi
    root = None 
    try:
        session = HTMLSession2()
        page = session.get(url)
        # Used html_requests to sup[port rendering of javascript
        page.html.render(sleep=sleep_time, timeout=20)
        root = page.html.html
        session.close()  
    except:
        print("Unable to load page: " + url)
    return root

# Scrape Affiliation data from web page using beautiful soup
def get_affiliations(doi):
    affiliations = list()    
    r = load_bs(doi + "#tab-contributors", 5)    
    if r == None:
        print("Unable to load html")
        return
    soup = BeautifulSoup(r, 'html.parser')
    #  get the divs with the author property
    results = soup.findAll("div", {"property" : "author"})
    for result in results:
        # From the div, get Author name information and the span with the name property
        # which contains the affiliation data for the authors
        family_names = result.findAll("span", {"property" : "familyName"})
        first_names = result.findAll("span", {"property" : "givenName"})
        affiliations_found = result.findAll("span", {"property" : "name"})
        name = ""
        # Combine first and last name
        if len(first_names) == 1:
            name += first_names[0].text.strip() + " "
        if len(family_names) == 1:
            name += family_names[0].text.strip()
        # Create list of affiliations
        for affiliation in affiliations_found:
            affiliations.append(affiliation.text)
    # Return the list of affiliations for the paper
    return affiliations
