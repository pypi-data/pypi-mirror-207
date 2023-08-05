"""RadioBrowser API Datatypes"""

from typing import NewType, TypeVar


NOT_SET = ""

UUID = NewType("UUID", str)
URL = NewType("URL", str)
T = TypeVar("T")


class Order:
    """Posible values of Order argument"""

    NAME = "name"
    URL = "url"
    HOMEPAGE = "homepage"
    FAVICON = "favicon"
    TAGS = "tags"
    COUNTRY = "country"
    STATE = "state"
    LANGUAGE = "language"
    VOTES = "votes"
    CODEC = "codec"
    BITRATE = "bitrate"
    LASTCHECKOK = "lastcheckok"
    LASTCHECKTIME = "lastchecktime"
    CLICKCOUNT = "clickcount"
    CLICKTREND = "clicktrend"
    CHANGETIMESTAMP = "changetimestamp"
    RANDOM = "random"


class Boolean:
    """RadioBrowser API Boolean datatype"""

    BOTH = "both"
    TRUE = "true"
    FALSE = "false"