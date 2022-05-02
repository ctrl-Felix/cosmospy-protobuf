from setuptools import setup


setup(
   name='cosmospy_protobuf',
   version='0.0.1',
   description='This package contains a compiled python version of all cosmos protobuf files with their dependencies.',
   author='ctrl-Felix',
   author_email='dev@ctrl-felix.de',
   packages=['cosmospy_protobuf'],
   package_dir={'cosmos': 'cosmospy_protobuf'},
   install_requires=[], #external packages as dependencies
)