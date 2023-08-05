"""RadioBrowser API Struct State"""

from msgspec import Struct

from typing import Optional


class State(Struct):
    """RadioBrowser API Struct State

    Attributes
    ----------------------------------------
    ``name`` : |str|, optional
        Name of the state

    ``country`` : |str|, optional
        Country of the state

    ``stationcount`` : |int|, optional
        Station state count
    """
    name: Optional[str] = None
    country: Optional[str] = None
    stationcount: Optional[int] = None