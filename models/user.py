#!/usr/bin/python3
"""

Module Defining User Class

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class that inherits from BaseModel

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user first name
        last_name (str): user last name
    """

    def __init__(self, *args, **kwargs):
        """Constructor for User Class """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
