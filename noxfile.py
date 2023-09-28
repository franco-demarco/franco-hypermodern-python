"This module setups Nox testing session"


import nox_poetry as nox


@nox.session(venv_backend="venv", python=["3.9", "3.8"])
def tests(session):
    """Run coverage tests

    Args:
        session (Session): Nox session
    """
    session.install("pytest", ".")
    session.install("coverage[toml]", ".")
    session.install("pytest-cov", ".")
    session.install("pytest-mock", ".")
    session.run("pytest", "--cov")
