from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from urllib.request import Request, urlopen

from DataExtractor.WorkerGenerator import WorkerGenerator
from .LinkCreator import LinkCreator


class RequestHTML:

    def __init__(self):

        self._ListPages = []
        self.CreateLink = LinkCreator()
        self.UserAgent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                          '(HTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        self._workers = WorkerGenerator()

    def get_pages_html(self, max_page):
        self._ListPages.clear()
        list_links = self.CreateLink.create_links_cars(int(max_page))
        self._workers.assign_worker(self._extract_page_html, list_links)
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

    def get_page_html_model(self, list_brand):
        self._ListPages.clear()
        temp_list = self.CreateLink.create_links_model(list_brand)
        self._workers.assign_worker(self._get_page_html_model, temp_list)
        return self._ListPages

    def _get_page_html_model(self, url):
        demand = Request(url, headers=self.UserAgent)
        page = urlopen(demand)
        page_html = page.read()
        self._ListPages.append(page_html)
        page.close()






