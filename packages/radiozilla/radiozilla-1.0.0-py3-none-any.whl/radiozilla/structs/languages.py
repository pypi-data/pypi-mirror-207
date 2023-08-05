"""RadioBrowser API Struct Language"""

from msgspec import Struct

from typing import Optional


class Language(Struct):
    """RadioBrowser API Struct Language

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the language

    ``iso_639`` : |str|, optional
        Standards by the International Organization for Standardization

    ``stationcount`` : |int|, optional
        Station language count
    """
    name: Optional[str] = None
    iso_639: Optional[str] = None
    stationcount: Optional[int] = None