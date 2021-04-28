1) Sites to be web scraped for a given domain:
crt.sh [confirmed] [done]
https://fofa.so/ [confirmed] [skipped]
https://subdomainfinder.c99.nl/ [confirmed] [done]
certspotter [confirmed] -- extraction for certificates of a website [will incorporate later]
threatcrowd [confirmed] use https://github.com/AlienVault-OTX/ApiV2 API [done]
Binaryedge [confirmed] -- limited 250 queries allowed so don't exhaust [might update later]
Intelx [confirmed]
Recon.dev [confirmed] -- very small dataset and query in free plan
Shodan [confirmed] use api
Spyse [confirmed] Good One use API [leaving, API not free and is having usecase higher than what we needed]
Virustotal [confirmed] try to find how we can incoprate this one
Zoomeye [confirmed]
DNSDumpster [confirmed] [done]
RapidDNS [confirmed]
Integration of waybackurls https://github.com/tomnomnom/waybackurls

2.1) Resolve all the subdomains to their ips [optional here]
2.2) Filter found subdomains using httpx
2.3) 


3) directory bruteforcing with a small customized list for the domains [not in P]


4) Parameter Mining using Arjun [not in P]


5) Check for Vulnerabilities [--attack]
- Check for Reflected XSS
- Check for Reflected LFI


Extras:
- Multiple Domain support

- CLI
    - Passive mode to skip anything active or else by default it's active
    - Attack mode to perform possible attacks
    - looks good https://github.com/guelfoweb/knock


## Notes:
- Keep it fail safe by using plug and use style
- dns.bufferover.run [don't work] :: funny


----------------------------------------------------------------------------------------------

- Once we have subdomaind, directories listed, params mined, attacks covered we then send the report to the user telegram
- Store onced performed report in database so to use it again (caching?) if not older than a week and --no-cache is not used
- Older results never get delted and are incorported in further scans from httpx

----------------------------------------------------------------------------------------------

Work on CLI

----------------------------------------------------------------------------------------------

Create a Web App for the result showcase more beautifully

----------------------------------------------------------------------------------------------

A basic app to start the search from it, Pay Per Scan, Results generated

----------------------------------------------------------------------------------------------

Start working on Research Paper @Akshit handle major work in this
Work on Improving the complete project
For ISM we don't need research paper and hence project gets over here

----------------------------------------------------------------------------------------------

Publish research paper by claiming it generates good results and does most of the recon work required in pentesting and hence should be used by BBH
for all of their work

----------------------------------------------------------------------------------------------


## Extras
- Add Proxy Option