#!/usr/bin/python3
"""

Module Defining Place Class

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class that inherits from BaseModel

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): place name
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max number of guests
        price_by_night (int): price by night
        latitude (float): place latitude
        longitude (float): place longitude
        amenity_ids (list): list of amenity ids
    """

    def __init__(self, *args, **kwargs):
        """Constructor for Place Class """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
