from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from urllib.request import Request, urlopen
from .LinkCreator import LinkCreator


class RequestHTML:

    def __init__(self):

        self._ListPages = []
        self.CreateLink = LinkCreator()
        self.UserAgent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                          '(HTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    def get_pages_html(self, max_page):
        list_links = self.CreateLink.create_links(int(max_page))

        with PoolExecutor(max_workers=6) as executor:
            for _ in executor.map(self._extract_page_html, list_links):
                pass

        return self._ListPages

    def _extract_page_html(self, url):
        demand = Request(url, headers=self.UserAgent)
        page = urlopen(demand)
        page_html = page.read()
        self._ListPages.append(page_html)
        page.close()

    def get_page_link(self):
        return self.CreateLink.get_main_link()

    def get_page_main_html(self):
        demand = Request(self.CreateLink.get_main_link(), headers=self.UserAgent)
        page = urlopen(demand)
        page_html = page.read()
        page.close()
        return page_html

    def get_page_html_model(self, brand):
        self.CreateLink.set_car_mark(brand)
        demand = Request(self.CreateLink.get_main_link(), headers=self.UserAgent)
        page = urlopen(demand)
        page_html = page.read()
        return page_html
        page.close()







