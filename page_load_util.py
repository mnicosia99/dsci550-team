from requests_html import HTMLSession
from lxml.html.soupparser import fromstring

import asyncio, pyppeteer

doi_org_url = "http://www.doi.org/"

class HTMLSession2(HTMLSession):
    
    @property
    def browser(self):
        if not hasattr(self, "_browser"):
            self.loop = asyncio.get_event_loop()
            # self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=True, args=['--no-sandbox', '--proxy-server=pxu28134-0:aeu2T4Giav0dOiYg0lsz@x.botproxy.net:8080']))
            self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=True, args=['--no-sandbox']))
        return self._browser
    
def load_article_page(doi, sleep_time = 1):
    # affiliationx contains map of affiliation to unique list of people, the len of list provides lab size
    url = doi_org_url + doi
    print(url)   
    root = None 
    try:
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36'}
        session = HTMLSession2()
        page = session.get(url)
        page.html.render(sleep=sleep_time, timeout=20)
        root = fromstring(page.html.html) 
        session.close()  
    except:
        print("Unable to load page: " + url)
    return root
