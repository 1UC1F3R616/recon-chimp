import requests
import json
from utils.read_config import config


def send_tg_notif(chat: str = config("TELEGRAM_CHAT_ID")) -> bool:
    """
    sends a telegram notification that work is completed
    """
    bot_token = config("TELEGRAM_BOT_TOKEN")

    url = f"https://api.telegram.org/bot${bot_token}/sendMessage"
    payload = json.dumps(
        {
            "chat_id": chat,
            "text": "workflow run completed.",
        }
    )
    headers = {"Content-Type": "application/json"}
    
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    return False
