"""The hypermodern Python project module."""


import textwrap

import click
import requests

from . import __version__
from .constants import API_URL


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project.
    """
    click.echo("Hello World!")
    with requests.get(API_URL, timeout=1) as response:
        response.raise_for_status()
        data = response.json()
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
