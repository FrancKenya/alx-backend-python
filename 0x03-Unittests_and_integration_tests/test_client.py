#!/usr/bin/env python3
"""A github org client unittest
"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, mock_get_json, org_name):
        """Test GithubOrgClient.org"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.called_with_once(client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        with patch("client.GithubOrgClient.org", new_callable=property) as org:
            payload = {"repos_url": "Hi there"}
            org.return_value = payload
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])
