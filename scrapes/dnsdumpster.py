############################################################################################
# By: Siddhartha
# URL: https://dnsdumpster.com
# Date-Modified: 28-April-2020
# Time avg: Time taken is under 30 seconds
############################################################################################

from requests import Session
from bs4 import BeautifulSoup

def dnsdumpster(domain):
    """
    :input: domain-name / hostname
    :return-type: list
    """

    #########################################################################################
    ## we first need to get the CSRF token and then make a post request with it, use Sessions
    #########################################################################################

    session = Session()

    fetch = session.get('https://dnsdumpster.com')
    soup = BeautifulSoup(fetch.text, 'html.parser')
    
    input_fields = soup.find_all('input')
    token = None
    for input_field in input_fields:
        if input_field.get('name') == 'csrfmiddlewaretoken':
            token = input_field.get('value')
    
    data = 'csrfmiddlewaretoken={}&targetip={}'.format(token, domain)

    headers = {
        'Host': 'dnsdumpster.com',
        'Connection': 'close',
        'Content-Length': '104',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://dnsdumpster.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://dnsdumpster.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    response = session.post('https://dnsdumpster.com/', headers=headers, data=data, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')[3] # 4 tables are here and our required index is 3 for subdomains table
    rows = tables.find_all('tr')
    subdomains = []

    for row in rows:
        subdomain = row.find('td').text
        subdomains.append(subdomain.strip())
    
    return subdomains

## Testing Code
# print(dnsdumpster('dscvit.com'))