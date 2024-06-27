#!/usr/bin/env python3

""" Running tests in utils module """

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch

from typing import Dict, Mapping, Sequence, Union

from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Exception
            ) -> None:
        """ test access_nested_map if it raises an a KeyError Exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test case for get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """ Test get_json expected output """
        mock_obj = {'json.return_value': test_payload}

        with patch('requests.get', return_value=Mock(**mock_obj)) as test_get:
            self.assertEqual(get_json(test_url), test_payload)
            test_get.assert_called_once_with(test_url)
