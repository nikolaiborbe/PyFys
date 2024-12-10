from .constants import Constants
from .masses import Masses
from .main import PyFysInternal

class PyFysFactory:
    def __call__(self):
        return PyFysInternal()
    
    @property
    def Masses(self):
        return Masses

    @property
    def Constants(self):
        return Constants

pyfys = PyFysFactory()
Masses = Masses
Constants = Constants

__all__ = ['Constants', 'Masses', 'pyfys']