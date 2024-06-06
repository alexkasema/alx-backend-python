#!/usr/bin/env python3

""" Type Checking using mypy """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ returns a list of items """
    zoomed_in: Tuple = [  # type: ignore
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in  # type: ignore


array = [12, 72, 91]

zoom_2x = zoom_array(array)  # type: ignore

zoom_3x = zoom_array(array, 3)  # type: ignore
