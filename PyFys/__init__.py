from .constants import Constants
from .masses import Masses
from .main import PyFys

def __call__():
    return PyFys()

__all__ = ['Constants', 'Masses']