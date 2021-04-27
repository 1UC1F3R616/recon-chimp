############################################################################################
# By: 1UC1F3R616
# URL: https://subdomainfinder.c99.nl
# Date-Modified: 27-April-2020
# Time avg: 
# Note: Had to reverse engineer
# Updare: Tried RE, Not Succeed in what I wanted so now we need to intercept the request and use the tokens from their when making a scan
# work-left: take data from config file
############################################################################################

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
    data = 'CSRF1013566176013524=CSRF110138824&CSRF1107542595702104=network104844821&CSRF1074232519428413=intruder102395829&CSRF1042148766674400=cracker106191388&CSRF1037538048420212=spambot102672058&CSRF1000346543054959=espionage108912247&CSRF1032055544559625=firewall101328885&CSRF1019931363851841=addict109152379&CSRF1050005833718553=counterfeiter107559221&CSRF1020245951830640=spambot104989441&CSRF1096552198521366=CSRF109611552&CSRF1002041487332118=honeypot107357348&CSRF1102977247150436=spammer107341411&CSRF1081099726055260=stalker105689788&CSRF1024132533889206=scammer103872046&CSRF1017799996918442=malware104347714&CSRF1034834089072190=subnet_ip106861488&CSRF1025291767856366=drudge101150230&CSRF1065737879143935=ipv4101030025&CSRF1058038210550748=stalker108056404&CSRF1080109221539261=cyber107980423&CSRF1084745217985019=spambot104063277&CSRF1010129492983026=Trojan109057859&CSRF1095349497421608=subnet_ip105426753&CSRF1005435740918959=vulnerability100370523&CSRF1037137301955191=spy110286266&CSRF1082016311375833=cyberspace109477503&CSRF1027615352072011=infiltrator102183920&CSRF1096965064825209=network110691996&CSRF1053946025837679=espionage101568554&CSRF1097293093439684=malware109531546&CSRF1084969866374297=cyberwar105070989&CSRF1104131552617686=cyberwar109061695&CSRF9843433218797932=cybercrime108913136&jn=JS+aan%2C+T+aangeroepen%2C+CSRF+aangepast&domain=dscvit.com&lol-stop-reverse-engineering-my-source-and-buy-an-api-key=fa5475d8fcfbea7fe8d175dc2600a9c196ffa5f2&scan_subdomains='

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


