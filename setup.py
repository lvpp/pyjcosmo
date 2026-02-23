from setuptools import setup, find_packages

setup(
    name="pyjcosmo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "py4j>=0.9",
    ],
    author="Rafael de Pelegrini Soares",
    description="Python wrapper for JCOSMO Java library",
    url="https://ufrgs.br/lvpp",
    python_requires='>=3.6',
)