"This module setups Nox testing session"


import tempfile

import nox


nox.options.sessions = "lint", "black"


@nox.session(python=["3.9", "3.8"])
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


@nox.session(python=["3.8", "3.9"])
def lint(session):
    """Run linting

    Args:
        session (Session): Nox session
    """
    args = session.posargs or ["src", "tests", "noxfile.py"]
    session.install(
        "flake8",
        "flake8-black",
        "flake8-import-order",
        "flake8-bugbear",
        "flake8-bandit",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.9"])
def black(session):
    """Run formatter

    Args:
        session (Session): Nox session
    """
    args = session.posargs or ["src", "tests", "noxfile.py"]
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    """Check the dependencies for known security vulnerabilities

    Args:
        session (Session): Nox session
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with=dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
