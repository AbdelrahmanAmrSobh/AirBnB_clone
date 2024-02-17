#!/usr/bin/python3
"""Test for user module"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing the class User"""

    def test_email(self):
        """test email"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """test password"""
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """test first name"""
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """test second name"""
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
