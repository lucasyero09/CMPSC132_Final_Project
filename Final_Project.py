import requests 
from bs4 import BeautifulSoup

class LaptopScraper:

    def __init__(self, url):
        self.url = url
        self.laptops = []
        self.filteredlaptops = []

    @property
    def _soup(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def scrape(self):

        #Finds all the thumbnails. These contain all the information we need
        attribute_list = self._soup.find_all('div', class_='card thumbnail')

        laptops = []

        for attribute in attribute_list:
            a = attribute.find('a', class_ = 'title')
            name = a['title'] if a else "N/A"

            span = attribute.find('span', itemprop = 'price')
            #Checks before if the value exists
            price = span.text.strip() if span else "N/A"

            p = attribute.find('p', attrs = {'data-rating': True})
            #Checks before if the value exists
            rating = p['data-rating'] if p else "N/A"

            laptops.append({'name': name, 'price': price, 'rating': rating})
        
        self.laptops = laptops



url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"



