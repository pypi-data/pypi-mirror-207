"""RadioBrowser API Struct Station Check Step"""

from msgspec import Struct

from typing import Optional, Union

from radiozilla.datatypes import UUID, URL


class StationCheckStep(Struct):
    """RadioBrowser API Struct Station Check Step

    Attributes:
    ----------------------------------------
    ``stepuuid`` : |str, UUID|, optional
        An unique id for this StationCheckStep.

    ``parent_stepuuid`` : |str, UUID|, optional
        An unique id for referencing another StationCheckStep.
        Is set if this step has a parent.

    ``checkuuid`` : |str, UUID|, optional
        An unique id for referencing a StationCheck.

    ``stationuuid`` : |str, UUID|, optional
        An unique id for referencing a Station.

    ``url`` : |str, URL|, optional
        The url that this step of the checking process handled.

    ``urltype`` : |str|, optional
        Does represent which kind of url it is. One of
        the following: STREAM, REDIRECT, PLAYLIST.

    ``error`` : |str|, optional
        URL to the homepage of the stream, so you can direct the
        user to a page with more information about the stream.

    ``creation_iso8601`` : |str|, optional
        Date and time of step creation.
    """

    stepuuid: Optional[Union[str, UUID]] = None
    parent_stepuuid: Optional[Union[str, UUID]] = None
    checkuuid: Optional[Union[str, UUID]] = None
    stationuuid: Optional[Union[str, UUID]] = None
    url: Optional[Union[str, URL]] = None
    urltype: Optional[str] = None
    error: Optional[str] = None
    creation_iso8601: Optional[str] = None