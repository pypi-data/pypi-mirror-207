"""Internal RadioBrowser API wrapper module"""

from random import choice
from socket import (
    getaddrinfo,
    gethostbyaddr,
    gaierror,
    herror,
    IPPROTO_TCP,
)
from typing import Union

from ..datatypes import URL
from ..decorators.memoizations import memoize


class Browser:
    """Internal RadioBrowser API wrapper class

    Attributes:
    ----------------------------------------
    ``base`` : property
        Base Radio Browser API url

    ``servers`` : property
        Radio Browser API servers
    
    ``lookup`` : method
        Reverse DNS lookup

    ``hosts`` : property
        Radio Browser API hosts

    ``url`` : property
        Pick random Radio Browser API url
    """

    def __init__(self) -> None:
        """"""
        ...

    @property
    @memoize
    def base(self) -> str:
        """Base Radio Browser API url"""
        return "api.radio-browser.info"

    @property
    @memoize
    def servers(self) -> list[Union[str, URL]]:
        """Radio Browser API servers"""
        try:
            data = getaddrinfo(host=f"all.{self.base}",
                               port=80, family=0, type=0,
                               proto=IPPROTO_TCP)
        except gaierror:
            ...
        else:
            if (data and (isinstance(data[0][4], tuple))):
                return [ip[4][0] for ip in data]

        return []

    def lookup(self, ip: str) -> str:
        """Reverse DNS lookup"""
        try:
            hostname, *_ = gethostbyaddr(ip)
        except herror:
            ...

        return hostname

    @property
    @memoize
    def hosts(self) -> list[Union[str, URL]]:
        """Radio Browser API hosts"""
        names = []

        for ip in self.servers:
            try:
                host = self.lookup(ip)
            except Exception:
                ...
            else:
                names.append(host)

        return names

    @property
    @memoize
    def url(self) -> Union[str, URL]:
        """Pick random Radio Browser API url"""
        host = choice(sorted(self.hosts))

        return f"https://{host}"