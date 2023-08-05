"""Main RadioBrowser API wrapper module"""

from asyncio import run
from typing import Any, Optional, Union

from aiohttp import ClientSession
from msgspec.json import decode

from . import __version__
from .decorators import memoize
from .api import Browser
from .datatypes import T, Order, Boolean, NOT_SET
from .structs import (
    Codec,
    Country,
    CountryCode,
    Language,
    State,
    Tag,
    Station,
)
from .defaults import (
    _default_order,
    _default_reverse,
    _default_hidebroken,
    _default_offset,
    _default_limit,
    _default_name_exact,
    _default_country_exact,
    _default_language_exact,
    _default_has_extended_info,
    _default_has_geo_info,
    _default_is_https,
    _default_state_exact,
    _default_tag_exact,
)


class Radio(Browser):
    """Main RadioBrowser API wrapper class
    
    Attribtes:
    ----------------------------------------
    ``codecs`` : property
        Get list of codecs

    ``countries`` : property
        Get list of countries

    ``countrycodes`` : property
        Get list of countrycodes

    ``languages`` : property
        Get list of languages

    ``states`` : property
        Get list of states
    
    ``tags`` : property
        Get list of tags
    
    ``stations`` : property
        Get list of stations

    ``search`` : method
        Search station
    """

    def __init__(self) -> None:
        """"""
        super().__init__()

        self.headers = {"User-Agent": f"radiozilla/{__version__}"}

    @memoize
    async def __get(self, type: T, endpoint: str, params: dict[str, Any]) -> T:
        """Asynchronous method for sending requests to RadioBrowser API

        Parameters:
        ----------------------------------------
        ``type`` : |T|, required
            Serialization of the response with type
        ``endpoint`` : |str|, required
            Endpoint to request of RadioBrowser API
        ``params`` : |dict |str, Any||, optional
            Parameters of request
        """
        url = f"{self.url}/json/{endpoint}"

        async with ClientSession(headers=self.headers) as session:
            async with session.get(url, params=params) as response:
                return decode(await response.content.read(), type=type)

    def codecs(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Codec]:
        """Get list of codecs

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[Country],
            endpoint="codecs",
            params=params
        ))

    def countries(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Country]:
        """Get list of countries

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[Country],
            endpoint="countries",
            params=params
        ))

    def countrycodes(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[CountryCode]:
        """Get list of countrycodes

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[CountryCode],
            endpoint="countrycodes",
            params=params
        ))

    def languages(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Language]:
        """Get list of languages

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[Language],
            endpoint="languages",
            params=params
        ))

    def states(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[State]:
        """Get list of states

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[State],
            endpoint="states",
            params=params
        ))

    def tags(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Tag]:
        """Get list of tags

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[Tag],
            endpoint="tags",
            params=params
        ))

    def stations(
        self,
        order: Optional[Union[str, Order]] = _default_order,
        reverse: Optional[Union[bool, Boolean]] = _default_reverse,
        offset: Optional[int] = _default_offset,
        limit: Optional[int] = _default_limit,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Station]:
        """Get list of stations

        Parameters:
        ----------------------------------------
        ``order`` : |str, Order|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        params = {
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }

        return run(self.__get(
            type=list[Station],
            endpoint="stations",
            params=params
        ))

    def search(
        self,
        name: Optional[str] = NOT_SET,
        name_exact: Optional[Union[str, Boolean]] = _default_name_exact,
        country: Optional[str] = NOT_SET,
        country_exact: Optional[Union[str, Boolean]] = _default_country_exact,
        countrycode: Optional[str] = NOT_SET,
        state: Optional[str] = NOT_SET,
        state_exact: Optional[Union[str, Boolean]] = _default_state_exact,
        language: Optional[str] = NOT_SET,
        language_exact: Optional[Union[str, Boolean]] = _default_language_exact,
        tag: Optional[str] = NOT_SET,
        tag_exact: Optional[Union[str, Boolean]] = _default_tag_exact,
        tag_list: Optional[str] = NOT_SET,
        codec: Optional[str] = NOT_SET,
        bitrate_min: Optional[str] = NOT_SET,
        bitrate_max: Optional[str] = NOT_SET,
        has_geo_info: Optional[Union[str, Boolean]] = _default_has_geo_info,
        has_extended_info: Optional[Union[str, Boolean]] = _default_has_extended_info,
        is_https: Optional[Union[str, Boolean]] =_default_is_https,
        order: Optional[Union[str, Order]] = NOT_SET,
        reverse: Optional[Union[str, Boolean]] = _default_reverse,
        offset: Optional[str] = NOT_SET,
        limit: Optional[str] = NOT_SET,
        hidebroken: Optional[Union[str, Boolean]] = _default_hidebroken,
    ) -> list[Station]:
        """Search station

        Parameters:
        ----------------------------------------
        ``name`` : |str|, optional
            Name of the station.

        ``name_exact`` : |str, Boolean|, optional
            True: only exact matches, otherwise all matches.

        ``country`` : |str|, optional
            Country of the station.

        ``country_exact`` : |str, Boolean|, optional
            True: only exact matches, otherwise all matches.

        ``countrycode`` : |str|, optional
            2-digit countrycode of the station (see ISO 3166-1 alpha-2).

        ``state`` : |str|, optional
            State of the station

        ``state_exact`` : |str, Boolean|, optional
            True: only exact matches, otherwise all matches.

        ``language`` : |str|, optional
            Language of the station

        ``language_exact`` : |str, Boolean|, optional
            True: only exact matches, otherwise all matches.

        ``tag`` : |str|, optional
            A tag of the station

        ``tag_exact`` : |str, Boolean|, optional
            True: only exact matches, otherwise all matches.

        ``tag_list`` : |str|, optional
            A comma-separated list of tag. It can also be an
            array of string in JSON HTTP POST parameters. All
            tags in list have to match.

        ``codec`` : |str|, optional
            Codec of the station

        ``bitrate_min`` : |str|, optional
            Minimum of kbps for bitrate field of stations in result

        ``bitrate_max`` : |str|, optional
            Maximum of kbps for bitrate field of stations in result

        ``has_geo_info`` : |str, Boolean|, optional
            Not set = display all;
            True = show only stations with geo_info;
            False = show only stations without geo_info.

        ``has_extended_info`` : |str, Boolean|, optional
            Not set = display all;
            True = show only stations which do provide extended information;
            False = show only stations without extended information.

        ``is_https`` : |str, Boolean|, optional
            Not set = display all;
            True = show only stations which have https url;
            False = show only stations that do stream unencrypted with http.

        ``order`` : |str|, optional
            Name of the attribute the result list will be sorted by.

        ``reverse`` : |str, Boolean|, optional
            Reverse the result list if set to true.

        ``offset`` : |str|, optional
            Starting value of the result list from the database.
            For example, if you want to do paging on the server side.

        ``limit`` : |str|, optional
            Number of returned datarows (stations) starting with offset.

        ``hidebroken`` : |str, Boolean|, optional
            Do list/not list broken stations.
        """
        arguments = {
            "name": name,
            "nameExact": name_exact,
            "country": country,
            "countryExact": country_exact,
            "countrycode": countrycode,
            "state": state,
            "stateExact": state_exact,
            "language": language,
            "languageExact": language_exact,
            "tag": tag,
            "tagExact": tag_exact,
            "tagList": tag_list,
            "codec": codec,
            "bitrateMin": bitrate_min,
            "bitrateMax": bitrate_max,
            "has_geo_info": has_geo_info,
            "has_extended_info": has_extended_info,
            "is_https": is_https,
            "order": order,
            "reverse": reverse,
            "offset": offset,
            "limit": limit,
            "hidebroken": hidebroken,
        }
        params = {}

        for argument in arguments.items():
            item, value = argument

            if value != NOT_SET:
                params[item] = value

        return run(self.__get(
            type=list[Station],
            endpoint="stations/search",
            params=params
        ))

