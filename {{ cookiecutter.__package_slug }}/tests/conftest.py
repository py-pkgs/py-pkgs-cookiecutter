import pytest


@pytest.fixture
def config_dict():
    return {"env": "dev", "pipeline": {"setting": "this"}}
