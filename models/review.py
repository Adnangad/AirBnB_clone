#!/usr/bin/python3
"""
This module contains class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a Subclass of BaseModel.
    """
    place_id = ''
    user_id = ''
    text = ''
