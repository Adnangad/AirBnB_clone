#!/usr/bin/python3
"""
This module contains a class
"""
import os.path
import json
from models.base_model import BaseModel


class FileStorage():
    """
    This module serializes and deserializes objects.
    """
    __file_path = "/AirBnB_clone/tests/test_models/file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the obj with a key.
        
        Args:
        obj: the obj to be set with a key.

        Return:
        None.
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes the obj to a file.
        """
        file_path = FileStorage.__file_path
        obj = FileStorage.__objects
        serialized_obj = {o: obj[o].to_dict() for o in obj.keys()}
        with open(file_path, "w") as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Desirializes the obj from a file.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                r = json.load(f)
                for dat in r.values():
                    clas_name = dat["__class__"]
                    del dat["__class__"]
                    self.new(eval(clas_name)(**dat))