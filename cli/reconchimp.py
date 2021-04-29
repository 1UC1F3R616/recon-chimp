import typer
from enum import Enum
from scrapes import crt_sh
from notification.notifier import send_tg_notif, send_discord_notif

app = typer.Typer()


class Notifiers(Enum):
    telegram = "telegram"
    discord = "discord"


@app.command()
def do_recon(
    domain: str = typer.Argument("", help="The domain name for the required host"),
    all: bool = typer.Option(True, help="Selects all available tools for recon"),
    notify: Notifiers = typer.Option("", help="Select notification service"),
):
    """
    performs reconnaissance on the supplied domain
    TODO: call the scrapers
    """

    if all:
        print(crt_sh.crt_sh(domain))
    else:
        """
        TODO: selection logic
        """

    if notify == Notifiers.telegram:
        print(send_tg_notif())
    elif notify == Notifiers.discord:
        send_discord_notif()


app()
"""
reconchimp dscvit.com --all --notify telegram|discord
"""
