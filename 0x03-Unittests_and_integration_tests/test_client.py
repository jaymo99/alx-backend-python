"""
test_client module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Case for GithubOrgClient.
    """
    @parameterized.expand([
        ("google", {"key": "value"}),
        ("abc", {"key": "another_value"}),
    ])
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org_name, expected_value, mock_get_json):
        """
        Assertion methods.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_value)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
