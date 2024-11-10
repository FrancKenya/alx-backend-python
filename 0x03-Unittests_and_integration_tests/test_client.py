#!/usr/bin/env python3
"""A github org client unittest
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos and
        use @patch as a decorator to mock get_json
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        Return:
            A payload of choice
        """
        payload = [{"name": "hello"}, {"name": "world"}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as public_mock:
            public_mock.return_value = "hello"
            client = GithubOrgClient("google")
            result = client.public_repos()
            expected = {item['name'] for item in payload}
            self.assertEqual(result, expected)
            public_mock.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Tests GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """method called to prepare the class for tests"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test for public repos without License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """method called after tests in an individual class have run"""
        cls.get_patcher.stop()
