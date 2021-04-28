## extrernal imports
import urllib.request

## internal imports
from scrapes.c99 import c99
from scrapes.crt_sh import crt_sh
from scrapes.dnsdumpster import dnsdumpster
from scrapes.threatcrowd import threatcrowd

domain = 'dscvit.com'

total_subdomains = set()

try:
    for subdomain in c99(domain):
        total_subdomains.add(subdomain)
except Exception as e:
    print('[!] Failed to fetch Subdomains from c99')
    print('[!] {}'.format(str(e)))

try:
    for subdomain in crt_sh(domain):
        total_subdomains.add(subdomain)
except Exception as e:
    print('[!] Failed to fetch Subdomains from cert.sh')
    print('[!] {}'.format(str(e)))

try:
    for subdomain in dnsdumpster(domain):
        total_subdomains.add(subdomain)
except Exception as e:
    print('[!] Failed to fetch Subdomains from dnsdumpster')
    print('[!] {}'.format(str(e)))

try:
    for subdomain in threatcrowd(domain):
        total_subdomains.add(subdomain)
except Exception as e:
    print('[!] Failed to fetch Subdomains from threatcrowd')
    print('[!] {}'.format(str(e)))

# total_subdomains =list(total_subdomains)

with open('temp_db/subdomains.txt', 'w') as f:
    for subdomain in total_subdomains:
        f.write(subdomain)
        f.write('\n')
