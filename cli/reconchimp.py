import typer
from enum import Enum

app = typer.Typer()


class Notifier(Enum):
    telegram = "telegram"
    discord = "discord"


@app.command()
def do_recon(
    domain: str = typer.Argument("", help="The domain name for the required host"),
    all: bool = typer.Option(True, help="Selects all available tools for recon"),
    notify: Notifier = typer.Option("", help="Select notification service"),
):
    """
    performs reconnaissance on the supplied domain
    """
    # print(domain, notify.name)


app()
"""
reconchimp dscvit.com --all --notify telegram|discord
"""
