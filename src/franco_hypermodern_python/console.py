"""Command-line interface."""

import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Main console.

    Args:
        language (str): Language edition of Wikipedia
    """
    data = wikipedia.random_info(language=language)
    title, extract = data.title, data.extract
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
