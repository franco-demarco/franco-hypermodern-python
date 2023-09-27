"""The hypermodern Python project module."""


import textwrap

import click

from . import __version__
from .wikipedia import random_info


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    click.echo("Hello World!")
    title, extract = random_info()
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
