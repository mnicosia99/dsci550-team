from requests_html import HTMLSession
from lxml.html.soupparser import fromstring

import asyncio, pyppeteer

#  all scraping starts by loading the doi.org url suffixed with the doi,
# this url will redirect to the actual web site the paper is published to
doi_org_url = "http://www.doi.org/"

#  Class to override the browser function so it runs headless
class HTMLSession2(HTMLSession):    
    @property
    def browser(self):
        if not hasattr(self, "_browser"):
            self.loop = asyncio.get_event_loop()
            self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=True, args=['--no-sandbox']))
        return self._browser

# Read the webpageand render the javascript, return the html object
def load_article_page(doi, sleep_time = 1):
    url = doi_org_url + doi
    print(url)   
    root = None 
    try:
        session = HTMLSession2()
        page = session.get(url)
        page.html.render(sleep=sleep_time, timeout=20)
        root = fromstring(page.html.html) 
        session.close()  
    except:
        print("Unable to load page: " + url)
    return root
