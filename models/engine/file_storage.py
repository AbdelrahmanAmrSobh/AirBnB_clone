#!/usr/bin/python3
"""
    module: responsible for serializes instances to a JSON file
            & deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
        the class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return the __objects dict which should contains all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            load obj into __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
            deserializes the json file to objects only if file exist
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    if value["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
