#!/usr/bin/python3
"""Test for amenity module"""

import unittest
from models.place import Place


class TestAmenity(unittest.TestCase):
    """testing the class Amenity"""

    def setUp(self):
        """create p"""
        self.p = Place()

    def test_city_id(self):
        """test city id"""
        self.assertEqual(str, type(self.p.city_id))

    def test_user_id(self):
        """test user id"""
        self.assertEqual(str, type(self.p.user_id))

    def test_name(self):
        """test name"""
        self.assertEqual(str, type(self.p.name))

    def test_description(self):
        """test description"""
        self.assertEqual(str, type(self.p.description))

    def test_number_rooms(self):
        """test number rooms"""
        self.assertEqual(int, type(self.p.number_rooms))

    def test_number_bathrooms(self):
        """test number bathrooms"""
        self.assertEqual(int, type(self.p.number_bathrooms))

    def test_max_guest(self):
        """test max guest"""
        self.assertEqual(int, type(self.p.max_guest))

    def test_price_by_night(self):
        """test price by night"""
        self.assertEqual(int, type(self.p.price_by_night))

    def test_latitude(self):
        """test latitude"""
        self.assertEqual(float, type(self.p.latitude))

    def test_longitude(self):
        """test longitude"""
        self.assertEqual(float, type(self.p.longitude))

    def test_amenity_ids(self):
        """test amenity ids"""
        self.assertEqual(list, type(self.p.amenity_ids))


if __name__ == "__main__":
    unittest.main()
