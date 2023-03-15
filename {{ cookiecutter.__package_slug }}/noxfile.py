import nox
import nox_poetry


@nox_poetry.session
def lint(session):
    session.install("flake8", ".")
    session.run("flake8", ".")
