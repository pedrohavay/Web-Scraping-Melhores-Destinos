import utils
import json
from bs4 import BeautifulSoup
from datetime import datetime

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
        html_promos = req.get_promos() # Get all promos
        promos = [] # Empty array for promos


        for x in html_promos:
            soup = BeautifulSoup(str(x), 'html.parser') # Transform to bs4
            promo_content = soup.find('div', class_="post-promo-home-c2") # Get div with informations
            a = promo_content.select_one('a[title]') # Get 'a' with title and url
            promos.append({'title': a.get_text(), 'url': a['href']}) # Append item in array of promos

        f = open('melhoresdestinos.json', 'w+') # Creating file or open file
        f.write(json.dumps({'timestamp': datetime. timestamp(datetime.now()), 'promos': promos})) # Write JSON in file

        print('\nPromoções salvas: melhoresdestinos.json')
        
    else : 
        print('Site Indisponível.')