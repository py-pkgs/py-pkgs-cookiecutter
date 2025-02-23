import sys
from importlib.metadata import (
    PackageNotFoundError,
    distribution,
)

MIN_CC_VERSION = "2.0.0"

def version(v):
    return tuple(map(int, (v.split("."))))


# assert cookiecutter >= 2.0.0
try:
    cc_version = version(distribution("cookiecutter").version)
except PackageNotFoundError:
    cc_version = None

min_version = version(MIN_CC_VERSION)
if cc_version is None or cc_version < min_version:
    print(
        f"ERROR: Please install cookiecutter >= {MIN_CC_VERSION} "
        f"(current version is {cc_version if cc_version else 'not installed'}):\n"
        f"\tpip install 'cookiecutter>=2', OR\n"
        f"\tconda install 'cookiecutter>=2'"
    )
    sys.exit(1)
