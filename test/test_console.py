"""
This module includes tests for the franco hypermodern python module.
"""

import click.testing
import pytest
from franco_hypermodern_python import console


@pytest.fixture(name="runner")
def fixture_runner():
    """Create click testing runner

    Returns:
        CliRunner: click testing runner
    """
    return click.testing.CliRunner()


@pytest.fixture(name="mock_requests_get")
def fixture_mock_requests_get(mocker):
    """Create mock for requests get method

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


def test_main_succeeds(runner, mock_requests_get):  # pylint: disable=W0613"
    """
    Running console main should succeed
    """
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):  # pylint: disable=W0613
    """
    Running console main should print title
    """
    result = runner.invoke(console.main)
    assert "Lorem ipsum" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    """
    Running console main should make a GET request
    """
    runner.invoke(console.main)
    assert mock_requests_get.called
