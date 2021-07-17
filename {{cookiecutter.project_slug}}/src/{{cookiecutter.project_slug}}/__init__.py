# importlib is included in the standard library for Python >= 3.8
# here __version__ is obtained from installed version of package
from importlib.metadata import version

__version__ = version(__name__)