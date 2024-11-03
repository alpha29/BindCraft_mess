import os
from importlib.metadata import version

__version__ = version(__package__)

MODULE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
