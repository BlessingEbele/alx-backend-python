#!/usr/bin/env python3
"""Unit tests for the utils.access_nested_map function."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: dict,
        path: tuple,
        expected: object
    ) -> None:
        """
        Test access_nested_map returns expected value for
        given nested_map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: dict,
        path: tuple
    ) -> None:
        """Test KeyError is raised for invalid path access."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))
#cla
"""
Test utils module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import utils


class TestGetJson(unittest.TestCase):
    """Test class for utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns expected result"""
        
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        # Patch requests.get to return our mock response
        with patch('requests.get', return_value=mock_response) as mock_get:
            # Call the function we're testing
            result = utils.get_json(test_url)
            
            # Assert that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)
            
            # Assert that the result equals the expected payload
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()