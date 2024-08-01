#!/usr/bin/python3
"""

Module Defining State Class

"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class that inherits from BaseModel

    Attributes:
        name (str): state name
    """

    def __init__(self, *args, **kwargs):
        """Constructor for State Class """
        self.name = ""
        super().__init__(*args, **kwargs)
