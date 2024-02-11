#!/usr/bin/python3
"""
This module contains class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This is a Subclass of BaseModel.
    """
    city_id = ''
    name = ''
    user_id = ''
    description = ''
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0)
    longitude = float(0)
    amenity_ids = ''
