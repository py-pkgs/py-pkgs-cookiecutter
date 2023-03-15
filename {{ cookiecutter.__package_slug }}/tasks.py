"""
This file contains PyInvoke commands <https://docs.pyinvoke.org/en/stable/getting-started.html>

View all tasks by executing `poetry run invoke --list`

Run a task by executing 'poetry run invoke <task>' on the command line.
"""

import datetime as dt
import logging
import os
import pathlib as plb
import typing

import git
from dotenv import load_dotenv
from invoke import task

from {{ cookiecutter.__package_slug }} import __version__

logger = logging.getLogger("tasks")
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

load_dotenv()

ENV_PREFIX = "MYPKG"  # Environment variable prefix
current_dir = plb.Path(__file__).absolute().parent

if os.getenv(f"{ENV_PREFIX}_ENV") == "prod" and os.getenv("RUNNER_OS") is None:
    print(
        "You are about to deploy to env=prod, but this is not a GitHub actions run. Are you sure that you want to continue?"
    )
    usr_input = input("Do you want to continue? (y/n)")
    if usr_input != "y":
        print("Quitting deployment!")
        exit()


def _check_environment_variable(v: typing.Union[typing.List[str], str]):
    if isinstance(v, str):
        return True if os.getenv(v) is not None else False
    else:
        return all([_check_environment_variable(lv) for lv in v])


def _get_commit_sha() -> str:
    repo = git.Repo(search_parent_directories=True)
    return repo.head.object.hexsha


def _create_docker_image_name(registry_url: str, flow_name: str) -> str:
    return os.path.join(registry_url, flow_name)


def _create_docker_tags(
    registry_url: str, flow_name: str, env: str
) -> typing.Tuple[str, str, str]:
    base = _create_docker_image_name(registry_url, flow_name)
    tag = f"{base}:latest-{env}"
    tag_sha = f"{base}:{_get_commit_sha()}"
    tag_version = f"{base}:{__version__}"
    return tag, tag_sha, tag_version


@task
def update_pip(c):
    """This will update pip in the virtual environment"""
    c.run("poetry run python -m pip install -U pip")


@task(
    help={
        "dev": "Install development dependency group",
        "docs": "Install docs dependency group",
    }
)
def install_dependencies(c, dev=False, docs=False):
    """Install project dependencies and optional dependencies"""
    update_pip(c)
    cmd = "poetry install"
    if dev:
        cmd += " --with dev"
    if docs:
        cmd += " --with docs"
    c.run(cmd)


@task
def remove_environment(c):
    """Remove all virtual environments associated with this project"""
    c.run("poetry env remove --all")


@task
def clean(c):
    """This will clean python artifacts"""
    c.run('find . -type f -name "*.py[co]" -delete')
    c.run('find . -type d -name "__pycache__" -delete')


@task
def set_up_pre_commit(c):
    """Set up pre-commit for the current project"""
    c.run("poetry run pre-commit install")


@task
def fmt(c):
    """Format python code using black"""
    c.run("poetry run black .")


@task
def lint(c):
    """Lint using flake8"""
    c.run("poetry run flake8 . --extend-exclude .notebooks")


@task
def type_check(c):
    """Check type hinting using mypy"""
    c.run("poetry run mypy . --exclude .notebooks --ignore-missing-imports")


@task
def sort_imports(c):
    """Sort python imports with isort"""
    c.run("poetry run isort . --skip .notebooks")


@task
def docstring_coverage(c):
    """Check docstring coverage using interrogate"""
    c.run("poetry run interrogate -vv src")


@task
def test(c):
    """Run pytest on the 'tests' directory"""
    print("Running tests ...")
    c.run(f'poetry run pytest {str(current_dir / "tests")}')


@task
def build_image(c):
    """Build docker image"""
    env = os.environ[f"{ENV_PREFIX}_ENV"]
    tag_latest, tag_sha, tag_version = _create_docker_tags(
        os.environ[f"{ENV_PREFIX}_DOCKER_REGISTRY_URL"],
        os.environ[f"{ENV_PREFIX}_DOCKER_IMAGE_NAME"],
        env,
    )
    cmd = f"DOCKER_BUILDKIT=1 docker build . -t {tag_latest}"
    if env in ["stg", "prod"]:
        cmd += f" -t {tag_sha}" + f" -t {tag_version}"
    c.run(cmd)


@task
def push_image(c):
    """Push docker image"""
    env = os.environ[f"{ENV_PREFIX}_ENV"]
    registry_url = os.environ[f"{ENV_PREFIX}_DOCKER_REGISTRY_URL"]
    docker_image_name = os.environ[f"{ENV_PREFIX}_DOCKER_IMAGE_NAME"]
    tag_latest, tag_sha, tag_version = _create_docker_tags(
        registry_url, docker_image_name, env
    )
    c.run(f"docker push {tag_latest}")
    if env in ["stg", "prod"]:
        c.run(f"docker push {tag_sha}")
        c.run(f"docker push {tag_version}")


@task
def build_and_push_image(c):
    """Build and push docker image"""
    build_image(c)
    push_image(c)
