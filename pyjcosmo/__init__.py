# pyjcosmo/__init__.py

# Import the main wrapper class so users can access it directly
from .core import JCosmoWrapper

# You can also define package-level metadata
__version__ = "0.1.3"
__author__ = "Rafael de Pelegrini Soares"

# Define what is exported when a user does 'from pyjcosmo import *'
__all__ = ["JCosmoWrapper"]