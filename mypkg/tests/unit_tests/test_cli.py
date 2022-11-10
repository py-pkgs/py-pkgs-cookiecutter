from typer.testing import CliRunner

from mypkg.cli import pipeline


def test_listings_cli():
    runner = CliRunner()
    result = runner.invoke(pipeline, ['/path/to/file.parquet'])
    assert result.exit_code == 0
