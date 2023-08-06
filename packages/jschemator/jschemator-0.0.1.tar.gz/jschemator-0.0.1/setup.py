from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="jschemator",
    version="0.0.1",
    description="A class interface for data modeling with json-schema",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
)
