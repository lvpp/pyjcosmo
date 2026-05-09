from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyjcosmo",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "py4j>=0.9",
    ],

    long_description=long_description,
    long_description_content_type='text/markdown',

    author="Rafael de Pelegrini Soares",
    description="Python wrapper for JCOSMO Java library",
    url="https://ufrgs.br/lvpp",
    python_requires='>=3.6',
)