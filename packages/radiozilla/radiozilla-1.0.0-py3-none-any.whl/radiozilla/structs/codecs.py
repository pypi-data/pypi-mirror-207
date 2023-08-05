"""RadioBrowser API Struct Codec"""

from msgspec import Struct

from typing import Optional


class Codec(Struct):
    """RadioBrowser API Struct Codec

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the codec

    ``stationcount`` : |int|, optional
        Station codec count
    """
    name: Optional[str] = None
    stationcount: Optional[int] = None