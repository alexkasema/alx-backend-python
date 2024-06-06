#!/usr/bin/env python3

""" Complex types - mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculate the sum of a list of float and int elements """
    return float(sum(mxd_lst))
