import sys

from pkg_resources import (
    get_distribution,
    packaging,
)

MIN_CC_VERSION = "2.0.0"

# assert cookiecutter >= 2.0.0
cc_version = packaging.version.parse(get_distribution("cookiecutter").version)
min_version = packaging.version.parse(MIN_CC_VERSION)
if cc_version < min_version:
    print(
        f"ERROR: please install cookiecutter >= {MIN_CC_VERSION} (current "
        f"version is {cc_version}):\n"
        f"\tpip install 'cookiecutter>=2', OR\n"
        f"\tconda install 'cookiecutter>=2'"
    )
    sys.exit(1)
