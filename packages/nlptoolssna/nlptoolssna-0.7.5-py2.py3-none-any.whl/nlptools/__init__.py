"""Top-level package for nlptools."""
import os
VERSION_FILE = os.path.join(os.path.dirname(__file__),
                            'nlptools',
                            'VERSION')
with open(VERSION_FILE, encoding='utf-8') as version_fp:
    VERSION = version_fp.read().strip()
__author__ = """Alaa' Omar"""
__email__ = 'alaa.omer2009@gmail.com'
__version__ = VERSION
