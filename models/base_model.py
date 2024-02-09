#!/usr/bin/python3
"""
This module contains the BaseModel class that will be used for this project.
"""
import datetime
import uuid


class BaseModel():
    """This class defines all other attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """
        This method initializes arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        val = datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
                    else:
                        setattr(self, key, val)

    def __str__(self):
        """
        This method returns the string rep of object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attr with the updates time.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
