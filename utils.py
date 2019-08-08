import requests

# Class with methods for Melhores Destinos 
class reqMD:
    def __init__(self, url):
        self.req = requests.get(url) # Execute request
    
    def get_status_code(self):
        return self.req.status_code
