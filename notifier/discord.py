import requests
import json
from utils.config import config


def send_discord_notif(url: str = config("DISCORD_WEBHOOK_URL")) -> bool:
    """
    sends a notification via discord webhook
    TODO: send analysis summary also (ref https://gist.github.com/Birdie0/78ee79402a4301b1faf412ab5f1cdcf9)
    """
    payload = json.dumps(
        {
            "content": "workflow run completed.",
        }
    )
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    return False
