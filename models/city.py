#!/usr/bin/python3
"""

Module Defining City Class

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class that inherits from BaseModel

    Attributes:
        state_id (str): state id
        name (str): city name
    """

    def __init__(self, *args, **kwargs):
        """Constructor for City Class """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
