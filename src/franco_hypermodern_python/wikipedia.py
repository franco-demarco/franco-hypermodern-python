""""
This module includes the random information retrieval
"""

import requests
import click
from .constants import API_URL


def random_info(language='en'):
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
        raise click.ClickException(error_message)
    return data["title"], data["extract"]
