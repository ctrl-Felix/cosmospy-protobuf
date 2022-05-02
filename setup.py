import os

from setuptools import setup, find_packages


setup(
    name='cosmospy_protobuf',
    version='0.0.1',
    description='This package contains a compiled python version of all cosmos protobuf files with their dependencies.',
    author='ctrl-Felix',
    author_email='dev@ctrl-felix.de',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True
)
