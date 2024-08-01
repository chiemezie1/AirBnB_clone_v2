#!/usr/bin/python3
"""

Module Defining Amenity Class

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class that inherits from BaseModel

    Attributes:
            name (str): amenity name
    """

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity Class """
        self.name = ""
        super().__init__(*args, **kwargs)
