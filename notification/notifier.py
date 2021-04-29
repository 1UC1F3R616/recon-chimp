import os
import json
from requests import request
# from .utils.config import config

############ PATHS ##############
path = os.path.abspath('')

config_file_path = os.path.join(path, '.config.json')
json_db = os.path.join(os.path.dirname(path), 'json_db')
#################################


with open(config_file_path, 'r') as json_data_file:
        data = json.load(json_data_file)
        TELEGRAM_CHAT_ID = data.get('TELEGRAM_CHAT_ID')
        TELEGRAM_BOT_TOKEN = data.get("TELEGRAM_BOT_TOKEN")


def send_tg_notif(chat: str = TELEGRAM_CHAT_ID) -> bool:
    """
    sends a telegram notification that work is completed
    TODO: add analysis data
    """
    bot_token = TELEGRAM_BOT_TOKEN

    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    payload = {"chat_id": chat, "caption": "Workflow run complete. File(s) attached."}

    files = [
        (
            "document",
            (
                "active_subdomains.txt",
                open("temp_db/active_subdomains.txt", "rb"),
                "text/plain",
            ),
        )
    ]

    response = request("POST", url, data=payload, files=files)
    if response.status_code == 200:
        return True
    print(response.status_code)
    return False

send_tg_notif()

# def send_discord_notif(url: str = config("DISCORD_WEBHOOK_URL")) -> bool:
#     """
#     sends a notification via discord webhook
#     TODO: send analysis summary also (ref https://gist.github.com/Birdie0/78ee79402a4301b1faf412ab5f1cdcf9)
#     """
#     payload = json.dumps(
#         {
#             "content": "workflow run completed.",
#         }
#     )
#     headers = {"Content-Type": "application/json"}

#     response = request("POST", url, headers=headers, data=payload)
#     if response.status_code == 204:
#         return True
#     print(response.status_code)
#     return False
