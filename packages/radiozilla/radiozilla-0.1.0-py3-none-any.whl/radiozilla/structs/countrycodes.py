"""RadioBrowser API Struct CountryCode"""

from msgspec import Struct

from typing import Optional


class CountryCode(Struct):
    """RadioBrowser API Struct CountryCode

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the countrycode

    ``stationcount`` : |int|, optional
        Station countrycode count
    """
    name: Optional[str] = None
    stationcount: Optional[int] = None