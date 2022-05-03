# read version from installed package
from importlib.metadata import version
__version__ = version("{{ cookiecutter.package_name.lower().replace(' ', '_').replace('-', '_') }}")