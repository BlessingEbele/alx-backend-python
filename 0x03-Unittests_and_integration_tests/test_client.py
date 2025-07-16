#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient.org method."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns expected data and
        calls get_json with correct URL.
        """
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
from unittest.mock import patch, PropertyMock  # Already likely imported


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns expected data and
        get_json is called with correct URL.
        """
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL based on mocked org."""
        test_url = "https://api.github.com/orgs/test-org/repos"

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": test_url}
            client = GithubOrgClient("test-org")
            self.assertEqual(client._public_repos_url, test_url)
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns correct list and mocks are called."""
        test_url = "https://api.github.com/orgs/test-org/repos"
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            return_value=test_url, 
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = test_url
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(test_url)
            mock_url.assert_called_once()
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns True only when license matches."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
