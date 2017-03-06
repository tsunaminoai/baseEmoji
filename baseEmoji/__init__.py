from pkg_resources import get_distribution

__version__ = get_distribution('baseEmoji').version

from .baseEmoji import encode
from .baseEmoji import encodeStr
from .baseEmoji import decode
from .baseEmoji import decodeStr