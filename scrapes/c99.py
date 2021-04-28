############################################################################################
# By: 1UC1F3R616
# URL: https://subdomainfinder.c99.nl
# Date-Modified: 27-April-2020
# Time avg: 
# Note: Had to reverse engineer
# Updare: Tried RE, Not Succeed in what I wanted so now we need to intercept the request and use the tokens from their when making a scan
############################################################################################

import os
import json
import requests
import bs4

BeautifulSoup = bs4.BeautifulSoup

### Old Code ###
# import urllib
# from requests import Session
# def c99(domain):
#     """
#     """
#     URL = 'https://subdomainfinder.c99.nl'

#     requests_ = Session()
#     fetch_tokens = requests_.get(URL)

#     soup = BeautifulSoup(fetch_tokens.text, 'html.parser')

#     hiddens = soup.find_all('input')

#     tokens = {}

#     for hidden in hiddens:
#         if (hidden.get('name') != None and hidden.get('value') != None):
#             tokens[hidden.get('name')] = hidden.get('value')
    
#     tokens['jn'] = 'JS aan, T aangeroepen, CSRF aangepast'
#     tokens['domain'] = domain
#     tokens['scan_subdomains'] = True

#     tokens = urllib.parse.urlencode(tokens)
#     print(tokens)
#     # fetch = requests_.post(URL, data=tokens, headers=dict(Referer=URL))
#     # print(fetch.text)
#     # with open('here.txt', mode='w') as f:
#     #     f.write(fetch.text)
#     print('done')
##################

############ PATHS ##############
path = os.path.abspath('')

config_file_path = os.path.join(path, '.config.json')
#################################

def c99(domain):
    """
    :input: domain name
    :return-type: list
    :return: subdomains
    """

    headers = {
        'Host': 'subdomainfinder.c99.nl',
        'Connection': 'close',
        'Content-Length': '1608',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://subdomainfinder.c99.nl',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://subdomainfinder.c99.nl/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Make a config file from where all files can be configured
    with open(config_file_path, 'r') as json_data_file:
        data = json.load(json_data_file)
        DATA = data.get('DATA')

    data = DATA

    response = requests.post('https://subdomainfinder.c99.nl/', headers=headers, data=data, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr')
    subdomains = []
    for row in rows:
        if len(row.find_all('td')) != 0:
            subdomains.append((row.find_all('td')[1]).find('a').text)
    
    return subdomains

## Testing code
# print(c99('dscvit.com'))


