from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="langgraph-agent",
    version="6.9",
    author="morshed",
    packages=find_packages(),
    install_requires = requirements,
)