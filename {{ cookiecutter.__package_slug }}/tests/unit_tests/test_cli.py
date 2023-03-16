from typer.testing import CliRunner
from {{cookiecutter.__package_slug}}.cli import app


def test_listings_cli():
    runner = CliRunner()
    result = runner.invoke(app, ["{{ cookiecutter.__package_slug }}", "/path/to/file.parquet"])
    assert result.exit_code == 0
