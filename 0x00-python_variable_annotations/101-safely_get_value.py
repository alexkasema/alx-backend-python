#!/usr/bin/env python3

""" More involved type annotations """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

Default = Union[T, None]

Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Res:
    """ return the value in a dictionary with the associated key """
    if key in dct:
        return dct[key]
    else:
        return default
