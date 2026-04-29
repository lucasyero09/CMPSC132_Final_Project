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


    def display(self):
        if not self.laptops:
            raise RuntimeError("No laptops found. Run scrape() first.")

        #Iterates through the dictionary and prints
        for laptop in self.laptops:
            print(f"Laptop: {laptop['name']}")
            print(f"Price: {laptop['price']}")
            print(f"Rating: {laptop['rating']} / 5")
            print("-" * 30)

    def display_filtered(self):
        if not self.filteredlaptops:
            raise RuntimeError("No filtered laptops found. Run filter() first.")

        #Iterates through the dictionary and prints
        for laptop in self.filteredlaptops:
            print(f"Laptop: {laptop['name']}")
            print(f"Price: {laptop['price']}")
            print(f"Rating: {laptop['rating']} / 5")
            print("-" * 30)


    @property
    def _name_filter(self):
        #Returns sorted list extracting the name from the nested dict and using that as the sorting criteria
        return sorted(self.laptops, key=lambda x: x['name'])

    @property
    def _price_filter(self):
        #Returns sorted list extracting the price and cleaning it by removing the $ from the nested dict and using that as the sorting criteria
        return sorted(self.laptops, key=lambda x: float(x['price'].replace('$', '')))

    @property
        #Returns sorted list extracting the rating from the nested dict and using that as the sorting criteria
    def _rating_filter(self):
        return sorted(self.laptops, key=lambda x: int(x['rating']))
    
    def filter(self, method, amount):

        VALID_FILTERS = ['Laptop', 'Price', 'Rating']

        #Input checks
        if method not in VALID_FILTERS:
            raise ValueError(f"Invalid filter method '{method}'. Choose from: 'Laptop', 'Price', 'Rating'")
        if amount is not None and not type(amount) == int:
            raise ValueError(f"Invalid amount '{amount}'. Please choose only non-zero positive integers or None")
        if amount is not None and amount <= 0:
            raise ValueError(f"Invalid amount '{amount}'. Please choose only non-zero positive integers or None")
                
        #Checks for each type of filter method
        if method == 'Laptop':
            self.filteredlaptops = self._name_filter
        elif method == 'Price':
            self.filteredlaptops = self._price_filter
        elif method == 'Rating':
            self.filteredlaptops = self._rating_filter

        #Filtering for the amount, keeping the amount listed
        if type(amount) == int:
            self.filteredlaptops = self.filteredlaptops[:amount]

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"




url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"



