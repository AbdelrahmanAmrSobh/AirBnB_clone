#!/usr/bin/python3
"""Test for city module"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """testing the class City"""

    def test_state_id(self):
        """test state id"""
        c = City()
        self.assertEqual(str, type(c.state_id))

    def test_name(self):
        """test name"""
        c = City()
        self.assertEqual(str, type(c.name))


if __name__ == "__main__":
    unittest.main()
