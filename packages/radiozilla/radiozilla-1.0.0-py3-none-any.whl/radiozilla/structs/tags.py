"""RadioBrowser API Struct Tag"""

from msgspec import Struct

from typing import Optional


class Tag(Struct):
    """RadioBrowser API Struct Tag

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the tag

    ``stationcount`` : |int|, optional
        Station tag count
    """
    name: Optional[str] = None
    stationcount: Optional[int] = None