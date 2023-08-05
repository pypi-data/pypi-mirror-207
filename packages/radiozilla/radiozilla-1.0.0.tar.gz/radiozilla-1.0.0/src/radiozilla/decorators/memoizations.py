"""Memoization module for optimizing requests"""

from typing import Callable, Any


def memoize(callback: Callable) -> Callable:
    """"""
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        item = str(args) + str(kwargs)

        if item not in cache:
            cache[item] = callback(*args, **kwargs)

        return cache[item]

    return wrapper