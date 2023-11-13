#!/usr/bin/python3
""""Defines the Place class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Class for representing a place

    Attributes:
        city_id (str): The city ID
        user_id (str): The user's ID
        name (str): name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms vailable
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The max number of guests
        price_by_night (int): The price per night
        latitude (float): The latitude
        longitude (float): The longitude
        amenity_ids (list): List of amenity IDs
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
