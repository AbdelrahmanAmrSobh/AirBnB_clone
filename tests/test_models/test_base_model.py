#!/usr/bin/python3
"""test for base model"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import models
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """The class that contains test cases for BaseModel"""

    def setUp(self):
        """save old storage"""
        try:
            os.rename(os.getcwd() + "/file.json", "tmp_storage")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        self.base_model = BaseModel()

    def tearDown(self):
        """remove tmp storage"""
        try:
            os.remove(os.getcwd() + "/file.json")
        except IOError:
            pass
        try:
            os.rename(os.getcwd() + "/tmp_storage", "file.json")
        except IOError:
            pass

    def test_init(self):
        """test init method"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """test save method"""
        old_time = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_time, self.base_model.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + self.base_model.id, f.read())

    def test_to_dict(self):
        """test to_dict method"""
        d_i = self.base_model.to_dict()
        self.assertIsInstance(d_i, dict)
        self.assertIn('id', d_i)
        self.assertIn('created_at', d_i)
        self.assertIn('updated_at', d_i)
        self.assertIn('__class__', d_i)

    def test_str(self):
        """test str method"""
        self.assertEqual(str(self.base_model),
                         "[BaseModel] ({}) {}".
                         format(self.base_model.id, self.base_model.__dict__))

    def test_id(self):
        """test unique id"""
        base_model = BaseModel()
        self.assertNotEqual(base_model.id, self.base_model.id)

    def test_created_at(self):
        """test created_at"""
        self.assertEqual(self.base_model.created_at,
                         self.base_model.updated_at)


if __name__ == "__main__":
    unittest.main()
