import nox_poetry


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def format_pyproject(session):
    """Format the project's pyproject.toml"""
    session.install("pyproject-fmt", ".")
    session.run("pyproject-fmt", "pyproject.toml")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def docstring_coverage(session):
    """Check coverage of docstrings"""
    session.install("interrogate", ".")
    session.run("interrogate", "-vv", "src")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def code_lint(session):
    """Code linting"""
    session.install("ruff", ".")
    session.run("ruff", "check", ".")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def format_code(session):
    """Format code with black"""
    session.install("black", ".")
    session.run("black", "-v", ".")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def security_lint(session):
    """Scan for security issues"""
    session.install("bandit", ".")
    session.run("bandit", "-v", ".")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def check_dependency_issues(session):
    """Check import / dependency issues"""
    session.install("deptry", ".")
    session.run("deptry", "src")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def sort_imports(session):
    """Sort imports"""
    session.install("isort", ".")
    session.run("isort", ".", "-v", "--diff")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def code_spelling(session):
    """Check for misspellings in code"""
    session.install("codespell", ".")
    session.run(
        "codespell", ".", "--skip", ".nox,.venv,.notebooks,docs,site,poetry.lock"
    )


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def check_type_hints(session):
    """Check type hints"""
    session.install("mypy", ".")
    session.run("mypy", ".")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def test(session):
    """Run pytest"""
    session.install("pytest", ".")
    session.install("pytest-helpers-namespace", ".")
    session.install("coverage", ".")
    session.run_always(
        "poetry", "install", "--without", "dev", "--without", "docs", external=True
    )
    session.run("coverage", "run", "-m", "pytest", "tests")


@nox_poetry.session(reuse_venv=True, python=["{{ cookiecutter.python_version }}"])
def build_docs(session):
    """Build project documentation"""
    session.install("mkdocs", ".")
    session.install("mkdocstrings[python]", ".")
    session.install("mkdocs-include-markdown-plugin", ".")
    session.install("mkdocs-jupyter", ".")
    session.install("mkdocs-material", ".")
    session.run("mkdocs", "build")
