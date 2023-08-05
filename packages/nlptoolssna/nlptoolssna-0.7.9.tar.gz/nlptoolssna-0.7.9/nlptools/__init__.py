"""Top-level package for nlptools."""
import os

# Read the version from the VERSION file
with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
    __version__ = f.read().strip()
__author__ = """Alaa' Omar"""
__email__ = 'alaa.omer2009@gmail.com'
#__version__ = '0.7.7'