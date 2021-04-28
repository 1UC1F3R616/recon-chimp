import json
from requests import request
from utils.config import config


def send_tg_notif(chat: str = config("TELEGRAM_CHAT_ID")) -> bool:
    """
    sends a telegram notification that work is completed
    TODO: add analysis data
    """
    bot_token = config("TELEGRAM_BOT_TOKEN")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps(
        {
            "chat_id": chat,
            "text": "workflow run completed.",
        }
    )
    headers = {"Content-Type": "application/json"}

    response = request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    print(response.status_code)
    return False


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

    response = request("POST", url, headers=headers, data=payload)
    if response.status_code == 204:
        return True
    print(response.status_code)
    return False
