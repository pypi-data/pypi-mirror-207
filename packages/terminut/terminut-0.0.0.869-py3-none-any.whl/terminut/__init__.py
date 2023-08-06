__title__ = 'terminut'
__author__ = 'vast#1337'
__version__ = '0.0.1a'

CURRENT_VERSION = '0.0.2'

from .console import *
from .customs import *


if __version__ < CURRENT_VERSION:
    printf(
        f"[TERMINUT] Version Out-of-Date. Please upgrade by using: \"python.exe -m pip install -U terminut\"", 
        mainCol=Fore.RED,
        showTimestamp=False
    )