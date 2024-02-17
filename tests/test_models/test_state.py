#!/usr/bin/python3
"""Test for state module"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """testing the class state"""

    def test_name(self):
        """test name"""
        s = State()
        self.assertEqual(str, type(s.name))


if __name__ == "__main__":
    unittest.main()
