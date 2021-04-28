############################################################################################
# By: Siddhartha
# URL: https://app.binaryedge.io/
# Date-Modified: 28-April-2020
# Time avg: Time taken is under 30 seconds
############################################################################################

import os
import json
import requests
import socket

############ PATHS ##############
path = os.path.abspath('')

config_file_path = os.path.join(path, '.config.json')
json_db = os.path.join(os.path.dirname(path), 'json_db')
#################################

def binaryedge(domain):

    with open(config_file_path, 'r') as json_data_file:
        data = json.load(json_data_file)
        BINARYEDGE_API_KEY = data.get('BINARYEDGE_API_KEY')

    headers = {
            'X-Key': BINARYEDGE_API_KEY,
        }
    
    ip = socket.gethostbyname(domain)

    ## Save API call by checking if the file already exists and if so then just load it's json response ##


    response = requests.get('https://api.binaryedge.io/v2/query/ip/{}'.format(ip), headers=headers)
    response_json = response.json()

    # writing json in a file to analyze and use later next time if it pre exists saving an api call
    json_object = json.dumps(response_json, indent = 4)
    
    with open('{}/{}.json'.format(json_db, ip), "w") as outfile:
        outfile.write(json_object)


## Testing code
binaryedge('dscvit.com')