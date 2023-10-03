"""
This module includes tests for the console module.
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


@pytest.fixture(name="mock_random_info")
def fixture_mock_random_info(mocker):
    """Create mock for requests get method

    Args:
        mocker (MockerFixture): Pytest mocker fixture

    Returns:
        MagicMock: Request get mock
    """
    return mocker.patch("franco_hypermodern_python.wikipedia.random_info")


def test_main_prints_title(
    runner, mock_requests_get_successful
):  # pylint: disable=W0613
    """
    Running console main should print title
    """
    result = runner.invoke(console.main)
    assert "Lorem ipsum" in result.output


def test_main_fails_gracefully_on_request_error(
    runner, mock_requests_get_failure
):  # pylint: disable=W0613
    """
    Running console main should fail gracefully on request error
    """
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specified_language(
    runner, mock_random_info
):  # pylint: disable=W0613
    """
    Retrieved article should be in the specified language
    """

    runner.invoke(console.main, ["--language=de"])
    mock_random_info.assert_called_with(language="de")
