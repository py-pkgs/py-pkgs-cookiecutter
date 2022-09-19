import logging
import click

logger = logging.getLogger("{{ cookiecutter.__package_slug }}.cli")


@click.command()
def pipeline():
    ...
