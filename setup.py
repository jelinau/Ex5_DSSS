from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflakes",
    version="0.1",
    author="DSSS",
    author_email="jelina.unger@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles", "matplotlib"],
)