import pathlib as plb
import tempfile
import typing

import yaml  # type: ignore

from {{ cookiecutter.__package_slug }}.config import load_config


def test_load_config(config_dict: typing.Dict[str, typing.Union[str, typing.Dict]]):
    with tempfile.TemporaryDirectory() as tmpdir:
        path_to_config = plb.Path(tmpdir) / "config.yaml"
        with path_to_config.open("w") as outFile:
            yaml.safe_dump(config_dict, outFile)
            _ = load_config(path_to_config)
