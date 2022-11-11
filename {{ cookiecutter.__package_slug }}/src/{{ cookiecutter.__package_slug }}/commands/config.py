import logging
import os
import pathlib as plb
import typing

import typer

from {{ cookiecutter.__package_slug }} import config as pipeline_config
from {{ cookiecutter.__package_slug }}.config import load_config
from {{ cookiecutter.__package_slug }}.const import _ENV_VAR_MAPPING

logger = logging.getLogger("{{ cookiecutter.__package_slug }}.commands.config")

config = typer.Typer(
    help="🗒  Create and/or validate a config file for a {{ cookiecutter.__package_slug }} pipeline.",
    no_args_is_help=True,
)


def _check_config_arg(
    key: str, value: typing.Optional[typing.Union[int, str, bool]]
) -> typing.Optional[typing.Union[int, str, bool]]:
    env_value: typing.Optional[typing.Union[str, int]] = os.getenv(
        _ENV_VAR_MAPPING[key]
    )
    if env_value is not None:
        if key in ["extract_cache_expiration_in_days"]:
            env_value = int(env_value)
        elif key in ["extract_cache_use_cache"]:
            env_value = True if env_value.lower() == "true" else False  # type: ignore
        logger.debug(
            f"Found environment variable {key}=={env_value}. This overrides value passed to 'create_config()'"
        )
        return env_value
    elif value is not None:
        return value
    else:
        raise ValueError(
            f"Input argument '{key}' must either be passed to the CLI or must be set as an environment variable '{_ENV_VAR_MAPPING[key]}'"
        )


@config.command(
    name="create", short_help="🗒  Create a configuration file to run a {{ cookiecutter.__package_slug }} pipeline."
)
def create_config(
    output_path: str = typer.Argument(
        None,
        help="Location where you would like to store the config (e.g. '/path/to/flows/config.yaml')",
    ),
    env: typing.Optional[str] = typer.Option(
        None, help="Stage of production (dev/stg/prod)"
    ),
    pipeline_setting: typing.Optional[str] = typer.Option(
        None, help="Name of the Prefect block that holds your GCP credentials"
    ),
):
    _output_path = plb.Path(output_path).absolute()
    if not _output_path.parent.exists():
        raise FileNotFoundError(
            f"Parent directory '{str(_output_path.parent)}' does not exist"
        )
    config_out = pipeline_config.GlobalConfig(
        env=_check_config_arg("env", env),
        pipeline=pipeline_config.PipelineSettings(setting = _check_config_arg("pipeline_setting", pipeline_setting)),
    )
    with _output_path.open("w") as outFile:
        for line in config_out.yaml():
            outFile.write(line)


@config.command(
    name="validate", short_help="✅ Validate a configuration file for a {{ cookiecutter.__package_slug }} pipeline."
)
def validate_config(
    path_to_config: str = typer.Argument(
        None, help="Full path to a Funda ETL config file."
    )
):
    _path_to_config = plb.Path(path_to_config).resolve()
    if not _path_to_config.exists():
        raise FileNotFoundError(f"Config file at '{path_to_config}' does not exist")
    _ = load_config(_path_to_config)
    logger.info("🙏 Config validation passed!")
