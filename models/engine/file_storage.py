#!/usr/bin/python3
"""
This module contains a class
"""
import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """
    This module serializes and deserializes objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj with a key.
        
        Args:
        obj: the obj to be set with a key.

        Return:
        None.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes the obj to a file.
        """
        file_path = self.__file_path
        obj = FileStorage.__objects
        serialized_obj = {o: obj[o].to_dict() for o in obj.keys()}
        with open(file_path, "w") as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Desirializes the obj from a file.
        """
        try:
            with open(self.__file_path, "r") as f:
                r = json.load(f)
                for dat in r.values():
                    clas_name = dat["__class__"]
                    del dat["__class__"]
                    self.new(eval(clas_name)(**dat))
        except FileNotFoundError:
            pass
