from .constants import Constants
from .masses import Masses
from .main import PyFys

pyfys = PyFys

def __new__(cls):
    return PyFys()

__all__ = ['Constants', 'Masses', 'main']