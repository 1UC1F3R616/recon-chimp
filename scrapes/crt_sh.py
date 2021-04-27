############################################################################################
# By: 1UC1F3R616
# URL: https://crt.sh/
# Date-Modified: 27-April-2020
############################################################################################

import requests
from bs4 import BeautifulSoup

def crt_sh(domain):
    """
    :input: domain name
    :return-type: list
    """
    query = 'https://crt.sh/?q={}'.format(domain)

    fetch = requests.get(query)

    ############################
    ## crt.sh ID
    ## Logged At
    ## Not Before
    ## Not After
    ## Common Name
    ## Matching Identities
    ## Issuer Name
    ############################

    ############################
    ## There are 2 Tables, We ne
    ## ed to scape the second on
    ## e for our purpose.
    ############################

    soup = BeautifulSoup(fetch.text, 'html.parser')
    
    subdomains = set()
    

    tables = soup.find_all('table')
    table_with_subdomains = tables[1]
    rows = table_with_subdomains.find_all('tr') # row[0] is somehow covering all rows, row[1] is not needed, start from row[2]
    ## row[1] might not exist, case being handled, gives empty list ##
    
    for row in rows[2:]:
        columns = row.find_all('td')
    
        total = []
        for x in columns:
            if (x.get('style')==None) and (x.find_all('a') == []):
                total.append(x)
        subdomains_only_column = total[-1]
        for subdomain in subdomains_only_column:
            if subdomain not in ['<br/>', '<br/>']:
                subdomains.add(subdomain)
    
    subdomain_list = list(subdomains)

    return subdomain_list

            


## Testing Code
print(crt_sh('dscvit2.com'))