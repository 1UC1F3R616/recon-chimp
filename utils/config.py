import os
import json


def load_config():
    """
    TODO: loads the .config.json file into memory
    """


def config(key: str) -> str:
    """
    gets the key from config, if loaded
    otherwise it loads the config into memory fist
    """
    path = os.path.dirname("")
    print('coming from config.py {}'.format(path))
    config_file_path = os.path.join(path, ".config.json")
    with open(config_file_path, "r") as json_data_file:
        data = json.load(json_data_file)
        return data.get(key)
