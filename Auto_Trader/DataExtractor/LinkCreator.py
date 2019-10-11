

class LinkCreator:

    def __init__(self):

        self._num_rcs = 0
        self._num_rcp = 15

        # self._car_mark = 'ford/'
        # self._car_model = 'expedition/'
        # self._car_year = 'yRng=2007%2C2019&'
        # self._car_mileage = 'oRng=10000%2C200000&'

        self._car_mark = ''
        self._car_model = ''
        self._car_year = ''
        self._car_mileage = ''

        self._link = "https://www.autotrader.ca/cars/{0:s}{1:s}qc/montreal/" \
                     "?rcp={2:s}&rcs={3:s}&srt=3&{4:s}{05:s}prx=500&" \
                     "prv=Quebec&loc=Montreal%2C%20Qc&hprc=False&wcp=False&" \
                     "sts=New-Used&inMarket=advancedSearch".format(self._car_mark, self._car_model, str(self._num_rcp),
                                                                   str(self._num_rcs), self._car_year, self._car_mileage
                                                                   )

        self._links = []

    def create_links(self, max_page):
        x = 0
        while x < max_page:
            self._links.append(self._link)
            self._next_page()
            x += 1
        return self._links

    def _refresh_page(self):
        self._link = "https://www.autotrader.ca/cars/{0:s}{1:s}qc/montreal/" \
                     "?rcp={2:s}&rcs={3:s}&srt=3&{4:s}{05:s}prx=500&" \
                     "prv=Quebec&loc=Montreal%2C%20Qc&hprc=False&wcp=False&" \
                     "sts=New-Used&inMarket=advancedSearch".format(self._car_mark, self._car_model, str(self._num_rcp),
                                                                   str(self._num_rcs), self._car_year, self._car_mileage
                                                                   )

    def _next_page(self):
        self._num_rcs += self._num_rcp
        self._refresh_page()

    def get_main_link(self):
        self._refresh_page()
        return self._link

    def set_car_mark(self, brand):
        self._car_mark = '{}/'.format(brand)
