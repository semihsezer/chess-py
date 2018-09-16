from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='chess-py', 
    packages=['chess'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
    )
