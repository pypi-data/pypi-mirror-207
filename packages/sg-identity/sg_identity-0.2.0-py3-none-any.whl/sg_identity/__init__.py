import sys
from typing_extensions import ParamSpec

P = ParamSpec("P")

__all__ = [
    "sometimes_identity"
]

PY39 = sys.version_info >= (3, 9)

def sometimes_identity(*args: P.args) -> P.args:
    """
    :param args: Any args you'd like
    :returns: the args given to the function
    :raises: RuntimeError if not running Python >= 3.9
    """
    if PY39:
        return args
    raise RuntimeError("This function is only available in Python >= 3.9")

def identity(*args: P.args) -> P.args:
    """
    :param args: Any args you'd like
    :returns: the args given to the function
    """
    return args
