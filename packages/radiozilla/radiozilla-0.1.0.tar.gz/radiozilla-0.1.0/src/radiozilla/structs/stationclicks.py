"""RadioBrowser API Struct Station Click"""

from typing import Optional, Union

from msgspec import Struct

from radiozilla.datatypes import UUID


class StationClick(Struct):
    """RadioBrowser API Struct Station Click

    Attributes:
    ----------------------------------------
    ``stationuuid`` : |str, URL|, optional
        An unique id for referencing a Station.

    ``clickuuid`` : |str, URL|, optional
        ...

    ``clicktimestamp_iso8601`` : |str, URL|, optional
        ...

    ``clicktimestamp`` : |str, URL|, optional
        ...
    """
    stationuuid: Optional[Union[str, UUID]] = None
    clickuuid: Optional[Union[str, UUID]] = None
    clicktimestamp_iso8601: Optional[Union[str, UUID]] = None
    clicktimestamp: Optional[Union[str, UUID]] = None
