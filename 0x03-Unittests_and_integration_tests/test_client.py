#!/usr/bin/env python3
""" Running tests on client module """

import unittest

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from fixtures import TEST_PAYLOAD

from requests import HTTPError


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

    def test_public_repos_url(self) -> None:
        """ test the _public_repos_url method in GithubOrgClient class """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_repo:
            mock_repo.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos',
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'https://api.github.com/orgs/google/repos',
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_test_json: MagicMock) -> None:
        """ test the public_repos method in GithubOrgClient class """
        test_payload = {
            'repos_url': 'https://api.github.com/orgs/google/repos',
            'repos': [
                {
                    "id": 1936771,
                    "node_id": "MDEwOlJlcG9zaXRvcnkxOTM2Nzcx",
                    "name": "truth",
                    "full_name": "google/truth",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "type": "Organization",
                    },
                    "description": "Fluent assertions for Java and Android",
                    "fork": False,
                    "forks": 255,
                    "created_at": "2011-06-22T18:55:12Z",
                    "updated_at": "2024-06-28T01:46:16Z",
                },
                {
                    "id": 3248507,
                    "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTA3",
                    "name": "ruby-openid-apps-discovery",
                    "full_name": "google/ruby-openid-apps-discovery",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "type": "Organization",
                    },
                    "description": None,
                    "fork": False,
                    "forks": 23,
                    "created_at": "2012-01-23T17:09:03Z",
                    "updated_at": "2023-03-29T17:10:50Z",
                },
            ]
        }
        mock_test_json.return_value = test_payload['repos']
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "truth",
                    "ruby-openid-apps-discovery",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_test_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "apache-2.0"}}, "apache-2.0", True),
        ({"license": {"key": "other"}}, "apache-2.0", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """ test the GithubOrgClient.has_license method """
        client = GithubOrgClient("google")
        client_license = client.has_license(repo, key)
        self.assertEqual(client_license, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_paylaod": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test on GithubOrgClient methods """
    @classmethod
    def setUpClass(cls) -> None:
        """ Set up initial fixtures for every test """
        url_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """ get the payload from the given url """
            if url in url_payload:
                return Mock(**{'json.return_value': url_payload[url]})
            return HTTPError

        cls.get_patcher = patch("request.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """ Remove the fixures set up after running the test """
        cls.get_patcher.stop()
