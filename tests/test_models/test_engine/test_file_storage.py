#!/usr/bin/python3
"""test file storage"""

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class testing"""

    def setUp(self):
        """save old storage"""
        try:
            os.rename(os.getcwd() + "/file.json", "tmp_storage")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def test_file_path(self):
        """test file_path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects(self):
        """test objects"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """test method all"""
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """test method new"""
        b = BaseModel()
        storage.new(b)
        self.assertIn("BaseModel." + b.id, storage.all().keys())
        self.assertIn(b, storage.all().values())

    def test_save(self):
        """test method save"""
        b = BaseModel()
        storage.new(b)
        storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + b.id, save_text)

    def test_reload(self):
        """test method reload"""
        b = BaseModel()
        storage.new(b)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
