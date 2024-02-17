#!/usr/bin/python3
"""Test for amenity module"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing the class Amenity"""

    def test_name(self):
        """test name"""
        a = Amenity()
        self.assertEqual(str, type(a.first_name))


if __name__ == "__main__":
    unittest.main()
