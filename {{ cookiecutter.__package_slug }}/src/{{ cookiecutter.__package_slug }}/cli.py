import logging

import typer

from {{ cookiecutter.__package_slug }} import __version__
from {{ cookiecutter.__package_slug }}.steps.example import nchar
from {{ cookiecutter.__package_slug }}.commands import config


logger = logging.getLogger("{{ cookiecutter.__package_slug }}")
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


app = typer.Typer(
    help="🧰 Example CLI for {{ cookiecutter.__package_slug }}",
    no_args_is_help=True,
)
app.add_typer(config.config, name="config")


@app.callback()
def main(trace: bool = False):
    if trace:
        logger.setLevel(logging.DEBUG)
        

@app.command(
    short_help="📌 Displays the current version number of the {{ cookiecutter.__package_slug }} library"
)
def version():
    print(__version__)


@app.command(
    short_help="Prints the number of characters in the input string"
)
def pipeline_entrypoint(input_file: str):
    logger.info("Starting pipeline ...")
    logger.debug(f"Ingesting file {input_file}")
    result = nchar(input_file)
    logger.debug(f"File path has {result} characters")
    logger.info("Finished pipeline ...")


def entrypoint():
    app()
