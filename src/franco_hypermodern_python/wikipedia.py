""""
This module includes the random information retrieval
"""

import requests
from .constants import API_URL


def random_info():
    """Retrieves random information from the Wikipedia

    Returns:
        Tuple(str, str): Random article's title and extract
    """
    with requests.get(API_URL, timeout=1) as response:
        response.raise_for_status()
        data = response.json()
    title = data["title"]
    extract = data["extract"]
    return title, extract
