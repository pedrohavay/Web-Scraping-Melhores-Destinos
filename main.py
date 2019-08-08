import utils

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
        print(req.get_promos())
    else : 
        print('Site Indisponível.')