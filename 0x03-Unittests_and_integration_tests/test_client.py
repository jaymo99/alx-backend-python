#!/usr/bin/env python3
"""
test_client module
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Case for GithubOrgClient.
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json',)
    def test_org(self, org_name, expected_value, mock_get_json):
        """
        Assertion methods for test_org.
        """
        mock_get_json.return_value = MagicMock(
            return_value=expected_value
        )
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_value)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self):
        """
        Unit test for GithubOrgClient._public_repos_url
        """
        expected_repos_url = "https://api.github.com/orgs/test_org/repos"
        payload = {"repos_url": expected_repos_url}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, expected_repos_url)

    @patch('client.get_json', return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_repo):
        """
        Test GithubOrgClient.public_repos
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as m:

            test_client = GithubOrgClient('holberton')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            m.assert_called_once()

        @parameterized.expand([
                ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
                ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
            ])
        def test_has_license(self, repo, key: str, expected: bool) -> None:
            """Tests the `has_license` method."""
            gh_org_client = GithubOrgClient("google")
            client_has_licence = gh_org_client.has_license(repo, key)
            self.assertEqual(client_has_licence, expected)
