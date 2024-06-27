#!/usr/bin/env python3
""" Running tests on client module """

import unittest

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import MagicMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """ test the GithubOrgClient methods"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, resp: Dict, func: MagicMock) -> None:
        """ Test the org method in GithubOrgClient class """
        func.return_value = MagicMock(return_value=resp)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), resp)
        func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
