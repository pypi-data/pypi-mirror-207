"""Just holds the version for the app"""

import os

HERE = os.path.dirname(__file__)
__INIT_PY__ = os.path.join(HERE, "__init__.py")

with open(__INIT_PY__, encoding="utf-8", mode="r") as f:
    lines = f.read().splitlines()
    lines = [line for line in lines if line.startswith("__version__")]
    if len(lines) != 1:
        raise RuntimeError("Cannot find version in __init__.py")
    VERSION = lines[0].split("=")[1].strip().strip('"')
