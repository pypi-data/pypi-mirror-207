# coding: utf-8

from   setuptools import setup, find_packages

from   encrypta.config.base import BaseConfig

NAME = "encrypta"
VERSION = BaseConfig.VERSION

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="Encrypta - Encyption/Decrypytion tools",
    author_email="monkeeferret@gmail.com",
    install_requires=REQUIRES,
    python_requires=">=3.11",
    packages=find_packages(),
) 