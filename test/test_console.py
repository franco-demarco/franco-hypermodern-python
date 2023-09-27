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


def test_main_succeeds(runner):
    """
    Running console main should succeed
    """
    result = runner.invoke(console.main)
    assert result.exit_code == 0
