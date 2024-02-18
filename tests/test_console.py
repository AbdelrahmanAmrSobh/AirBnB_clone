#!/usr/bin/python3
"""Test console"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """class for testing"""

    class_is_missing = "** class name missing **"
    class_not_found = "** class doesn't exist **"
    id_is_missing = "** instance id missing **"
    id_not_found = "** no instance found **"
    attribute_is_missing = "** attribute name missing **"
    value_is_missing = "** value missing **"

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

    def test_quit(self):
        """test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertTrue(len(f.getvalue()) == 0)
        self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """test EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertTrue(len(f.getvalue()) == 0)
        self.assertEqual("", f.getvalue())

    def test_help(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertTrue(len(f.getvalue()) != 0)
        msg = "\nDocumented commands (type help <topic>):"
        self.assertTrue(f.getvalue().startswith(msg))

    def test_emptyline(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual("", f.getvalue())

    def test_function_class_name(self):
        """
        test create, show, destroy, all and update with class name
        """
        classes = [" BaseModel ", " User ", " Place ", " State ",
                   " City ", " Amenity ", " Review "]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create" + class_name)
                object_id = f.getvalue()
                self.assertTrue(len(object_id) != 0)
                self.assertNotEqual(object_id,  "")
                self.assertNotEqual(object_id, TestConsole.class_not_found)
                length = len(f.getvalue().split('\n'))
                HBNBCommand().onecmd("update" + class_name +
                                     object_id + " age 18")
                self.assertEqual(length, len(f.getvalue().split('\n')))
                HBNBCommand().onecmd("show" + object_id)
                object_dict = f.getvalue().split('\n')[1]
                self.assertTrue(len(object_dict) != 0)
                self.assertNotEqual(object_dict,  "")
                self.assertNotEqual(object_dict, TestConsole.id_not_found)
                self.assertTrue(storage.all()[class_name[1:-1] + "." +
                                              object_id[:-1]].age == "18")
                length = len(f.getvalue().split('\n'))
                HBNBCommand().onecmd("destroy" + class_name + object_id)
                self.assertEqual(len(f.getvalue().split('\n')), length)
                HBNBCommand().onecmd("all" + class_name)
                response = f.getvalue().split('\n')[2]
                self.assertTrue(len(response) == 2, response)
                self.assertEqual(response, "[]")

    def test_class_name_function(self):
        """
        test class name with all, count, show, destroy, update <attr> <value>
        and update <dict>.
        """
        classes = ["BaseModel", "User", "Place", "State",
                   "City", "Amenity", "Review"]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
                object_id = f.getvalue()[:-1]
                key = class_name + "." + object_id
                self.assertNotEqual(object_id, TestConsole.class_not_found)
                self.assertTrue(len(object_id) != 0)
                HBNBCommand().onecmd(class_name + ".count()")
                count = f.getvalue().split('\n')[1]
                self.assertEqual(count, "1")
                HBNBCommand().onecmd(class_name + f".show()")
                response1 = f.getvalue().split('\n')[2]
                self.assertEqual(response1, TestConsole.id_is_missing)
                HBNBCommand().onecmd(class_name + f".show({object_id[:-1]})")
                response1 = f.getvalue().split('\n')[3]
                self.assertEqual(response1, TestConsole.id_not_found)
                HBNBCommand().onecmd(class_name + f".show({object_id})")
                response1 = f.getvalue().split('\n')[4]
                self.assertNotEqual(response1, TestConsole.id_not_found)
                self.assertTrue(len(response1) != 0)
                HBNBCommand().onecmd(class_name + f".all()")
                response2 = f.getvalue().split('\n')[5]
                self.assertEqual(response2[2:-2], response1)
                HBNBCommand().onecmd(class_name + f".update()")
                response1 = f.getvalue().split('\n')[6]
                self.assertEqual(response1, TestConsole.id_is_missing)
                HBNBCommand().onecmd(class_name + f".update({object_id[:-1]})")
                response1 = f.getvalue().split('\n')[7]
                self.assertEqual(response1, TestConsole.id_not_found)
                HBNBCommand().onecmd(class_name + f".update({object_id})")
                response1 = f.getvalue().split('\n')[8]
                self.assertEqual(response1, TestConsole.attribute_is_missing)
                length = len(f.getvalue().split('\n'))
                HBNBCommand().onecmd(class_name + f".update({object_id},\
 {{last_name: tom, wife: mariam}})")
                self.assertEqual(length, len(f.getvalue().split('\n')))
                self.assertEqual(storage.all()[key].last_name, 'tom')
                self.assertEqual(storage.all()[key].wife, "mariam")
                HBNBCommand().onecmd(class_name + f".update({object_id},\
 first_name)")
                response1 = f.getvalue().split('\n')[9]
                self.assertEqual(response1, TestConsole.value_is_missing)
                length = len(f.getvalue().split('\n'))
                HBNBCommand().onecmd(class_name + f".update('{object_id}',\
 {{'first_name': 'John', \"age\": 89}})")
                self.assertEqual(length, len(f.getvalue().split('\n')))
                self.assertEqual(storage.all()[key].first_name, 'John')
                self.assertEqual(storage.all()[key].age, "89")
                HBNBCommand().onecmd(class_name + f".update('{object_id}',\
 'first_name', \"not_john\")")
                self.assertEqual(length, len(f.getvalue().split('\n')))
                self.assertNotEqual(storage.all()[key].first_name, 'John')
                self.assertEqual(storage.all()[key].first_name, 'not_john')
                HBNBCommand().onecmd(class_name + f".destroy()")
                response1 = f.getvalue().split('\n')[10]
                self.assertEqual(response1, TestConsole.id_is_missing)
                HBNBCommand().onecmd(class_name + f".destroy({object_id[:-1]})"
                                     )
                response1 = f.getvalue().split('\n')[11]
                self.assertEqual(response1, TestConsole.id_not_found)
                length = len(f.getvalue().split('\n'))
                HBNBCommand().onecmd(class_name + f".destroy({object_id})")
                self.assertEqual(length, len(f.getvalue().split('\n')))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyClass.all()")
            response = f.getvalue()
            self.assertEqual(response[:-1], TestConsole.class_not_found)


if __name__ == "__main__":
    unittest.main()
