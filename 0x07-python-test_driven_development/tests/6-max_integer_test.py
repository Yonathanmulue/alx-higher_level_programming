#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        result = max_integer([-1, -5, -2, -10])
        self.assertEqual(result, -1)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        result = max_integer([1, 2, 2, 4])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
