from pathlib import Path

import pytest

TEST_BASE_DIR = Path(__file__).parent.resolve()


@pytest.helpers.register  # type: ignore
def test_dir():
    return TEST_BASE_DIR


@pytest.fixture
def config_dict():
    return {"env": "dev", "pipeline": {"setting": "this"}}
