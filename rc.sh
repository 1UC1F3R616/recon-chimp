#!/bin/bash
python3 main.py
httpx -l temp_db/subdomains.txt -no-color -follow-host-redirects -status-code -title -content-length -web-server -silent >> temp_db/active_subdomains.txt

httpx -l temp_db/subdomains.txt -no-color -follow-host-redirects -silent >> temp_db/ffuf_subdomains.txt

i=0
while IFS= read -r line; do
    i=$((i+1))
    echo $i
    filename="/home/kush/Desktop/github/recon-chimp/temp_db/ffuf_resolved/ffuf_resolved${i}.json"

    ffuf -w dirlist.txt -u $line/FUZZ -o "${filename}"
done < temp_db/ffuf_subdomains.txt
