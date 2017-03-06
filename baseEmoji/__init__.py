import sys,os
VERSION_TUPLE = tuple(open(os.path.join('./', 'VERSION')).read().strip().split('.'))
VERSION = ".".join(map(str, VERSION_TUPLE))

from .baseEmoji import encode
from .baseEmoji import encodeStr
from .baseEmoji import decode
from .baseEmoji import decodeStr