"""Top-level package for nlptools."""
import os

# Read the version from the VERSION file
print(os.getcwd())
# with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
#     __version__ = f.read().strip()

VERSION_FILE = os.path.join(os.path.dirname(__file__),
                           
                            'VERSION')
with open(VERSION_FILE, encoding='utf-8') as version_fp:
    VERSION = version_fp.read().strip()
__author__ = """Alaa' Omar"""
__email__ = 'alaa.omer2009@gmail.com'
__version__ = VERSION