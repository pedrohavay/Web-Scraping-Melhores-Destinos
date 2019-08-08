import requests
from bs4 import BeautifulSoup

# Class with methods for Melhores Destinos 
class reqMD:
    def __init__(self, url):
        self.req = requests.get(url) # Execute request
    
    def get_status_code(self):
        return self.req.status_code

    def get_content(self):
        return self.req.content

    def get_promos(self):
        soup = BeautifulSoup(self.get_content(), 'html.parser')
        return soup.find_all('div', class_='promocao')
