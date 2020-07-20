from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

def test_version():
    assert __version__ == {{cookiecutter.version}}