VERSION_TUPLE = (0, 0, 1)
VERSION = ".".join(map(str, VERSION_TUPLE))

from .baseEmoji import encode_emoji
from .baseEmoji import encode_emoji_string
from .baseEmoji import decode_emoji
from .baseEmoji import decode_emoji_string