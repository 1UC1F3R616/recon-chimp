############################################################################################
# By: Akshit
# URL: https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=
# Date-Modified: 28-April-2020
# Time avg: Time taken is under 30 seconds
############################################################################################

import requests

def threatcrowd(domain):
    """
    :input: domain-name
    :return: subdomains
    :return-type: list
    """
    url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain)
    fetch = requests.get(url)

    subdomains = []

    for subdomain in (fetch.json()).get('subdomains'):
        subdomains.append(subdomain)

    return subdomains

## Test Code
# print(threatcrowd('vit.ac.in'))
## No result for dscvit.com
