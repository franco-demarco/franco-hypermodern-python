"This module setups Nox testing session"


import nox


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """Run coverage tests

    Args:
        session (Session): Nox session
    """
    session.run("poetry", "install", "--with=dev", external=True)
    session.run("pytest", "--cov", external=True)
