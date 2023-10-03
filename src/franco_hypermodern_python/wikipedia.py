""""
This module includes the random information retrieval
"""

from dataclasses import dataclass

import click
import requests
import desert
import marshmallow

from .constants import API_URL


@dataclass
class Page:
    """
    Page schema dataclass
    """

    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_info(language: str = "en") -> Page:
    """Retrieves random information from the Wikipedia

    Args:
    language (str, optional): _description_. Defaults to 'en'.

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
