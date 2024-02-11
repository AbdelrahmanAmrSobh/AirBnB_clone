#!/usr/bin/python3
"""
    BaseModel: the basic module for all future modules
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
        BaseModel: blueprint for future modules
    """

    def __init__(self, *args, **kwargs):
        """
            __init__: function that create instanse
            the function can create instance or load
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            __str__: returns the string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            save: update variable
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            to_dict: returns the dict containing the instance
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = result["created_at"].isoformat()
        result["updated_at"] = result["updated_at"].isoformat()
        return result
