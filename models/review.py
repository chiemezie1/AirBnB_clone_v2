#!/usr/bin/python3
"""

Module Defining Review Class

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class that inherits from BaseModel

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): review text
    """

    def __init__(self, *args, **kwargs):
        """Constructor for Review Class """
        self.user_id = ""
        self.place_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
