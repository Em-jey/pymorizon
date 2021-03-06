import os
import sys

version = '0.0.1'

VERSION = tuple(map(int, version.split('.')))
__version__ = VERSION
__versionstr__ = version

if (2, 7) <= sys.version_info < (3, 6):
    import logging

    DEBUG = os.environ.get('DEBUG')

    logger = logging.getLogger('morizon')
    logging.basicConfig(level=logging.DEBUG)

BASE_URL = 'https://www.morizon.pl'
