"""Client for the Wikipedia REST API, version 1."""

from dataclasses import dataclass

import click
import desert
import marshmallow
import requests

from .constants import API_URL


@dataclass
class Page:
    """Page resource.

    Attributes:
        title (str): The title of the Wikipedia article.
        extract (str): A plain text summary of the Wikipedia article.
    """

    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_info(language: str = "en") -> Page:
    """Retrieves random information from the Wikipedia.

    Args:
    language (str, optional): Wikipedia article language. Defaults to 'en'.

    Raises:
        click.ClickException: Connection Error

    Returns:
        Tuple(str, str): Random article's title and extract
    """
    try:
        with requests.get(API_URL % language, timeout=1) as response:
            response.raise_for_status()
            data = response.json()
    except requests.RequestException as error:
        error_message = str(error)
        raise click.ClickException(error_message) from error
    return schema.load(data)
