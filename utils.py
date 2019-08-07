import requests

# Class with methods for Melhores Destinos 
class ReqMD:
    def __init__(self, url):
        self.req = requests.get(url) # Execute request
    
    def get_status_code():
        return self.req.status_code
