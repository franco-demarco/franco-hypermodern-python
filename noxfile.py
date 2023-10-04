"""This module setups Nox testing session."""


import tempfile

import nox

locations = ["src", "tests", "noxfile.py"]
PACKAGE = "franco_hypermodern_python"


@nox.session(python=["3.9", "3.8"])
def cov_tests(session):
    """Run coverage tests.

    Args:
        session (Session): Nox session
    """
    session.install(".", "pytest", "coverage[toml]", "pytest-cov", "pytest-mock")
    session.run("pytest", "--cov")


@nox.session(python=["3.9", "3.8"])
def typeguard_tests(session):
    """Run tests with type checking.

    Args:
        session (Session): Nox session
    """
    session.install(".", "pytest", "pytest-mock", "typeguard")
    session.run("pytest", f"--typeguard-packages={PACKAGE}")


@nox.session(python=["3.8", "3.9"])
def lint(session):
    """Run linting.

    Args:
        session (Session): Nox session
    """
    args = session.posargs or ["src", "tests"]
    session.install(
        "flake8",
        "flake8-black",
        "flake8-import-order",
        "flake8-bugbear",
        "flake8-bandit",
        "flake8-annotations",
        "flake8-docstrings",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.9"])
def black(session):
    """Run formatter.

    Args:
        session (Session): Nox session
    """
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    """Check the dependencies for known security vulnerabilities.

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


@nox.session(python=["3.8", "3.9"])
def mypy(session):
    """Static type check.

    Args:
        session (Session): Nox session
    """
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python=["3.8", "3.9"])
def pytype(session):
    """Run static type checker.

    Args:
        session (Session): Nox session
    """
    args = session.posargs or ["--disable=import-error", *locations]
    session.install("pytype")
    session.run("pytype", *args)


@nox.session(python=["3.8"])
def xdoctest(session):
    """Run examples with xdoctest.

    Args:
        session (Session): Nox session
    """
    args = session.posargs or ["all"]
    session.install(".", "xdoctest", "pygments")
    session.run("xdoctest", PACKAGE, *args)


@nox.session(python=["3.8"])
def sphinx(session):
    """Build the documentation.

    Args:
        session (Session): Nox session
    """
    session.install("sphinx")
    session.run("sphinx-build", "docs", "docs/_build")
