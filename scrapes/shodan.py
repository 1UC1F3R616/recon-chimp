############################################################################################
# By: BRO3886
# URL: https://developer.shodan.io/
# Date-Modified: 28-April-2020
# Time avg: Time taken is under 30 seconds
############################################################################################

import os
import json
from shodan import Shodan

############ PATHS ##############
path = os.path.abspath("")

config_file_path = os.path.join(path, ".config.json")
json_db = os.path.join(os.path.dirname(path), "json_db")
#################################


def run_shodan(host: str):

    with open(config_file_path, "r") as json_data_file:
        data = json.load(json_data_file)
        SHODAN_API_KEY = data.get("BINARYEDGE_API_KEY")

    api = Shodan(SHODAN_API_KEY)

    # Lookup an IP
    ipinfo = api.host(host)
    print(ipinfo)

    # # Search for websites that have been "hacked"
    # for banner in api.search_cursor('http.title:"hacked by"'):
    #     print(banner)

    # # Get the total number of industrial control systems services on the Internet
    # ics_services = api.count("tag:ics")
    # print("Industrial Control Systems: {}".format(ics_services["total"]))
