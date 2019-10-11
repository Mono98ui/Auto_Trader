from Firestore.ServerComm import ServerComm
from .RequestHTML import RequestHTML
from bs4 import BeautifulSoup as Soup
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Extractor:

    def __init__(self):
        self._client = RequestHTML()
        self._sum_price_car = 0
        self._DataBase = ServerComm()
        # self._web_driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__))+'/WebDriver/chromedriver.exe')

    def extract_data(self):

        nbr_car = 0
        # max_page = self._extract_max_page()
        max_page = 2
        pages_html = self._client.get_pages_html(max_page)

        for page_html in pages_html:

            page_soup = Soup(page_html, "lxml")

            car_containers = page_soup.find_all("div", {"class": "result-item-inner"})

            for car in car_containers:
                car_price = car.find("span", {"class": "price-amount"}).get_text().lstrip('$').replace(',', '')
                self._sum_price_car += float(car_price)
                car_link = car.find("a", {"class": ["result-title", "click"]}).get('href')
                nbr_car += 1
                car_name = car.find("span", {"itemprop": "itemOffered"}).get_text().strip()
                print(car_name)

        return self._sum_price_car

    def _extract_max_page(self):
        page = self._client.get_page_link()
        self._web_driver.get(page)

        html_list = self._web_driver.find_element_by_xpath("//ul[contains(@class, 'col-xs-12') "
                                                           "and contains(@class, 'pagination')]")
        items = html_list.find_elements_by_tag_name("li")
        page_size = len(items) - 1
        max_page = items[page_size].get_attribute('data-page')
        self._web_driver.close()
        self._web_driver.quit()
        return max_page

    def extract_brands(self):

        clean_name = ""
        list_brand = []
        page_html = self._client.get_page_main_html()
        page_soup = Soup(page_html, "lxml")

        list_brands = page_soup.findAll("ul", {"id": "rfMakes"})

        for brand in list_brands:
            brand_names = brand.findAll("a")

            for name in brand_names:
                separate_name = str(name.text).split(' ')

                for x in range(len(separate_name)-1):
                    clean_name += separate_name[x]+" "

                # Temporaire
                # self._DataBase.create_brands(clean_name.strip())
                list_brand.append(clean_name.strip())
                clean_name = ""

        return list_brand

    def extract_model(self, brands):

        clean_name = ""

        page_html = self._client.get_page_html_model('ford')
        # page_html = self._client.get_page_main_html()
        page_soup = Soup(page_html, "lxml")

        list_brands = page_soup.findAll("ul", {"id": "rfModel"})

        for brand in list_brands:
            brand_names = brand.findAll("a")

            for name in brand_names:
                separate_name = str(name.text).split(' ')

                for x in range(len(separate_name) - 1):
                    clean_name += separate_name[x] + " "

                print(clean_name.strip())
                clean_name = ""

    def extract_years(self):
        page = self._client.get_page_link()
        self._web_driver.get(page)
        years_range = self._web_driver.find_element_by_css_selector("select[data-value='Min Year']")
        options = [x for x in years_range.find_elements_by_tag_name("option")]

        iterator_year = iter(options)
        next(iterator_year)

        for year in iterator_year:
            print(year.get_attribute("value"))

        self._web_driver.close()
        self._web_driver.quit()




