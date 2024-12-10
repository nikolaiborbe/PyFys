from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

DESCRIPTION = "A library that was made to quickly make physics projects."
LONG_DESCRIPTION = """This library was made to: 
1. Quickly graph equations by removeing customizability and focusing on simplicity.
2. Store all useful physics constants and equations.
3. Convert units easily.

This projects focus is heavily on simplicity and speed.
"""

# Setting up
setup(
    name="pyfys",
    version="0.2.4",
    author="Nikolai G. Borbe",
    url="https://github.com/nikolaiborbe",
    author_email="nikolaiborbe@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["matplotlib", "numpy"],
    keywords=['python', 'physics', 'graphing', 'constants'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)