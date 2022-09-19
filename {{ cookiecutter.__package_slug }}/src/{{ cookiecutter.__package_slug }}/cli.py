import logging

import click

logger = logging.getLogger("{{ cookiecutter.__package_slug }}.cli")
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)


@click.command()
@click.argument("input_file")
def pipeline(input_file):
    logger.info("Starting pipeline ...")
    logger.debug(f"Ingesting file {input_file}")
    ...
