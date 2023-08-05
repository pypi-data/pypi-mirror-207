"""RadioBrowser API Struct Country"""

from msgspec import Struct

from typing import Optional


class Country(Struct):
    """RadioBrowser API Struct Country

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the country

    ``iso_3166_1`` : |str|, optional
        Standard defining codes 

    ``stationcount`` : |int|, optional
        Station country count
    """
    name: Optional[str] = None
    iso_3166_1: Optional[str] = None
    stationcount: Optional[int] = None