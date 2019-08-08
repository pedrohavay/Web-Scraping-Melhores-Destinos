import utils
from bs4 import BeautifulSoup

if __name__ == '__main__':
    req = utils.reqMD('https://www.melhoresdestinos.com.br') # Instance ReqMD class
    status_code = req.get_status_code() # Get HTTP code
    print('''
===================
HTTP Code: %s
===================
''' % status_code)

    if status_code == 200:
        print('Site Disponível.\n\nObtendo informações...')
    else : 
        print('Site Indisponível.')