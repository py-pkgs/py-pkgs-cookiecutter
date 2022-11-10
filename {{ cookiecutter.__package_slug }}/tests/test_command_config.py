import os
import pathlib as plb
import tempfile

import pytest
import yaml  # type: ignore
from typer.testing import CliRunner

from flow_utils.commands import config

runner = CliRunner()


class TestCheckConfigArg:
    def test_check_config_arg_no_env_var(self):
        value = config._check_config_arg("env", "dev")
        assert value == "dev"

    def test_check_config_arg_environment_variable_with_bool_conversion(self):
        os.environ["FUNDA_ETL_EXTRACT_CACHE_USE_CACHE"] = "false"
        value = config._check_config_arg("extract_cache_use_cache", True)
        assert not value

    def test_check_config_arg_raises(self):
        with pytest.raises(
            ValueError,
            match="Input argument 'extract_cache_use_cache' must either be passed",
        ):
            if os.getenv("FUNDA_ETL_EXTRACT_CACHE_USE_CACHE") is not None:
                del os.environ["FUNDA_ETL_EXTRACT_CACHE_USE_CACHE"]
            _ = config._check_config_arg("extract_cache_use_cache", None)


def test_create_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            config.config,
            [
                "create",
                f"{tmpdir}/config.yaml",
                "--env",
                "dev",
                "--credentials-block",
                "my-credentials",
                "--extract-output-bucket",
                "this-bucket",
                "--extract-output-blob",
                "this-blob",
                "--extract-cache-use-cache",
                "--extract-cache-expiration-in-days",
                "4",
                "--extract-cache-storage-bucket",
                "this-bucket",
                "--extract-cache-storage-blob",
                "this-blob",
                "--transform-output-bucket",
                "this-bucket",
                "--transform-output-blob",
                "this-blob",
                "--load-output-dataset",
                "this-dataset",
                "--load-output-table",
                "this-table",
            ],
        )
    assert result.exit_code == 0


def test_validate_config(config_dict):
    with tempfile.TemporaryDirectory() as tmpdir:
        path_to_config = plb.Path(tmpdir) / "config.yaml"
        with path_to_config.open("w") as outFile:
            yaml.safe_dump(config_dict, outFile)
            runner.invoke(config.config, ["validate", path_to_config])
