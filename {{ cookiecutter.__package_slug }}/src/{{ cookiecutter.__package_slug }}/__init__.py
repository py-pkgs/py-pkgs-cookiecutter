"""{{ cookiecutter.package_name }} package."""

# Read version from installed package
from importlib.metadata import version

__version__ = version("{{ cookiecutter.__package_slug }}")
__author__ = "{{ cookiecutter.author_name }}"
__license__ = "{{ cookiecutter.open_source_license }}"
__description__ = "{{ cookiecutter.package_short_description }}"


# Public objects of the package (if any)
__all__ = []
"""list: List of public objects of the {{ cookiecutter.package_name }} package."""