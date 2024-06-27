#!/usr/bin/env python3

""" Running tests in utils module """

import unittest
from parameterized import parameterized

from typing import Dict, Mapping, Sequence, Union

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test case for access_nested_map method """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int],
            ) -> None:
        """ test access_nested_map output """
        self.assertEqual(access_nested_map(nested_map, path), expected)
