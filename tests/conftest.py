"""This module includes all shared pytest fixtures."""

import pytest
import requests


@pytest.fixture(name="mock_requests_get_successful")
def fixture_mock_requests_get_successful(mocker):
    """Create mock for requests get method.

    Args:
        mocker (MockerFixture): Pytest mocker fixture

    Returns:
        MagicMock: Request get mock
    """
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


@pytest.fixture(name="mock_requests_get_failure")
def fixture_mock_requests_get_failure(mock_requests_get_successful):
    """Create failing mock for requests get method.

    Args:
        mocker (MockerFixture): Pytest mocker fixture

    Returns:
        MagicMock: Failing request get mock
    """
    mock_requests_get_successful.side_effect = requests.RequestException
    return mock_requests_get_successful
