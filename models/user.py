#!/usr/bin/python3
"""
This module contains a class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from BaseModel.

    Attributes:
    email: empty str
    password: empty str
    first_name: empty str
    last_name: empty str
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
