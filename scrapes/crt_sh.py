############################################################################################
# By: 1UC1F3R616
# URL: https://crt.sh/
# Date-Modified: 27-April-2020
############################################################################################

import requests
from bs4 import BeautifulSoup

def crt_sh(domain):
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
    subdomains = []
    tables = soup.find_all('table')
    table_with_subdomains = tables[1]
    print(table_with_subdomains)



## Testing Code
crt_sh('vit.ac.in')