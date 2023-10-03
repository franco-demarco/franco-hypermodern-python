"""
This module include tests for the wikipedia module.
"""

from franco_hypermodern_python import wikipedia


def test_select_language(mock_requests_get_successful):
    """
    Should request an article in the specified language
    """
    wikipedia.random_info(language="de")
    requested_url = mock_requests_get_successful.call_args[0][0]
    assert "de.wikipedia.org" in requested_url


def test_random_page_returns_page(
    mock_requests_get_successful,
):  # pylint: disable=W0613
    """
    Should return a Page object
    """
    page = wikipedia.random_info()
    assert isinstance(page, wikipedia.Page)
