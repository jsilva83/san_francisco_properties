# Import external modules.
from bs4 import BeautifulSoup
import requests as req

# Constants.
URL_TO_WEBSCRAP = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22' \
                  'usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-' \
                  '122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is' \
                  'MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%' \
                  '7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afa' \
                  'lse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%' \
                  '22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds' \
                  '%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


class SanFranciscoWebScrap:

    def __init__(self, in_web_link: str):
        self.sf_link = in_web_link
        sf_response = req.get(url=in_web_link)
        sf_html_page_str = sf_response.text
        self.sf_soup = BeautifulSoup(markup=sf_html_page_str, features='html.parser')
        return

    def webscrap_addresses(self) -> list:
        out_addresses = []
        out_addresses = self.sf_soup.find_all(name='address', class_='list-card-addr')
        return out_addresses

    def webscrap_prices(self) -> list:
        out_prices = []
        out_addresses = self.sf_soup.find_all(name='div', class_='list-card-price')
        return out_prices

    def webscrap_web_links(self) -> list:
        out_links = []
        out_addresses = self.sf_soup.find_all(name='a', class_='list-card-link list-card-link-top-margin')
        return out_links
