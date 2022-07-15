import json
import subprocess
from itertools import product
from pathlib import Path

from pytest import (
    fixture,
    mark,
)

IGNORE = [".DS_Store", "__pycache__"]


@fixture()
def base_command(tmpdir):
    return (f"cookiecutter . --no-input --output-dir {tmpdir}", tmpdir)


def num_items(path, directory=[""]):
    files = [
        file
        for file in path.joinpath(*directory).iterdir()
        if file.name not in IGNORE
    ]
    return len(files)


def test_cookiecutter_default_options(base_command):
    result = subprocess.run(base_command[0], shell=True)
    assert result.returncode == 0


with open("cookiecutter.json") as f:
    options = json.load(f)
combinations = list(
    product(options["open_source_license"], options["include_github_actions"])
)


@mark.parametrize("open_source_license,include_github_actions", combinations)
def test_cookiecutter_all_options(
    base_command, open_source_license, include_github_actions
):
    params = f' open_source_license="{open_source_license}" include_github_actions={include_github_actions}'
    path = Path(base_command[1]).joinpath("mypkg")
    result = subprocess.run(base_command[0] + params, shell=True)
    assert result.returncode == 0
    assert num_items(path, ["tests"]) == 1
    assert num_items(path, ["src/mypkg"]) == 2
    assert num_items(path, ["docs"]) == 9
    print(f"Checking pair: {open_source_license}, {include_github_actions}")
    if open_source_license == "None":
        if include_github_actions in ["ci", "ci+cd"]:
            assert num_items(path, [".github", "workflows"]) == 1
            assert num_items(path) == 11
        else:
            assert num_items(path) == 10
    else:
        if include_github_actions in ["ci", "ci+cd"]:
            assert num_items(path, [".github", "workflows"]) == 1
            assert num_items(path) == 12
        else:
            assert num_items(path) == 11
