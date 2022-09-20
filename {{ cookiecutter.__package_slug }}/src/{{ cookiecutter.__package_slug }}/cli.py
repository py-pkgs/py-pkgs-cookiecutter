import logging

import click

from .steps.example import nchar

logger = logging.getLogger("{{ cookiecutter.__package_slug }}.cli")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)


@click.command()
@click.argument("input_file")
def pipeline(input_file):
    logger.info("Starting pipeline ...")
    logger.debug(f"Ingesting file {input_file}")
    result = nchar(input_file)
    logger.debug(f"File path has {result} characters")
