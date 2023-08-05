"""RadioBrowser API Struct Station Check"""

from typing import Optional, Union

from msgspec import Struct

from radiozilla.datatypes import UUID, URL


class StationCheck(Struct):
    """RadioBrowser API Struct Station Check

    Attributes:
    ----------------------------------------
    ``checkuuid`` : |str, UUID|, optional
        An unique id for this StationCheck.

    ``stationuuid`` : |str, UUID|, optional
        An unique id for referencing a Station.

    ``source`` : |str|, optional
        DNS Name of the server that did the stream check.

    ``codec`` : |str|, optional
        High level name of the used codec of the stream.
        May have the format AUDIO or AUDIO/VIDEO.

    ``bitrate`` : |int|, optional
        Bitrate 1000 bits per second (kBit/s) of the stream. (Audio + Video)

    ``hls`` : |int|, optional
        1 means this is an HLS stream, otherwise 0.

    ``ok`` : |int|, optional
        1 means this stream is reachable, otherwise 0.

    ``timestamp_iso8601`` : |str|, optional
        Date and time of check creation.

    ``timestamp`` : |str|, optional
        Date and time of check creation.

    ``urlcache`` : |str, URL|, optional
        Direct stream url that has been resolved from the
        main stream url. HTTP redirects and playlists
        have been decoded. If hls==1 then this is still a HLS-playlist.

    ``metainfo_overrides_database`` : |int|, optional
        1 means this stream has provided extended information and
        it should be used to override the local database, otherwise 0.

    ``public`` : |int|, optional
        1 that this stream appears in the public
        shoutcast/icecast directory, otherwise 0.

    ``name`` : |str|, optional
        The name extracted from the stream header.

    ``description`` : |str|, optional
        The description extracted from the stream header.

    ``tags`` : |str|, optional
        Komma separated list of tags. (genres of this stream)

    ``countrycode`` : |str|, optional
        Official countrycodes as in ISO 3166-1 alpha-2.

    ``countrysubdivisioncode`` : |str|, optional
        Official country subdivision codes as in ISO 3166-2.

    ``homepage`` : |str|, optional
        The homepage extracted from the stream header.

    ``favicon`` : |str|, optional
        The favicon extracted from the stream header.

    ``loadbalancer`` : |str|, optional
        The loadbalancer extracted from the stream header.

    ``server_software`` : |str|, optional
        The name of the server software used.

    ``sampling`` : |int|, optional
        Audio sampling frequency in Hz.

    ``timing_ms`` : |int|, optional
        Timespan in miliseconds this check needed to be finished.

    ``languagecodes`` : |str|, optional
        The description extracted from the stream header.

    ``ssl_error`` : |int|, optional
        1 means that a ssl error occured while
        connecting to the stream, 0 otherwise.

    ``geo_lat`` : |int|, optional
        Latitude on earth where the stream is located.

    ``geo_long`` : |int|, optional
        Longitude on earth where the stream is located.
    """

    checkuuid: Optional[Union[str, UUID]] = None
    stationuuid: Optional[Union[str, UUID]] = None
    source: Optional[str] = None
    codec: Optional[str] = None
    bitrate: Optional[int] = None
    hls: Optional[int] = None
    ok: Optional[int] = None
    timestamp_iso8601: Optional[str] = None
    timestamp: Optional[str] = None
    urlcache: Optional[Union[str, URL]] = None
    metainfo_overrides_database: Optional[int] = None
    public: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[str] = None
    countrycode: Optional[str] = None
    countrysubdivisioncode: Optional[str] = None
    homepage: Optional[str] = None
    favicon: Optional[str] = None
    loadbalancer: Optional[str] = None
    server_software: Optional[str] = None
    sampling: Optional[int] = None
    timing_ms: Optional[int] = None
    languagecodes: Optional[str] = None
    ssl_error: Optional[int] = None
    geo_lat: Optional[int] = None
    geo_long: Optional[int] = None