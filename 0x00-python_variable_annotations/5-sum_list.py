#!/usr/bin/env python3

""" Complex types - list of floats """

import functools
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ calculate the sum of floats in the list """
    return float(functools.reduce(lambda a, b: a + b, input_list))
