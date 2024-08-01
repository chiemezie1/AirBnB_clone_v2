#!/usr/bin/python3
"""

Module Defining State Class

"""

from models.city import City
from models.base_model import BaseModel, Base

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models
import sqlalchemy

class State(BaseModel):
    """
    State Class that inherits from BaseModel

    Attributes:
        name (str): state name
    """

    def __init__(self, *args, **kwargs):
        """Constructor for State Class """
        if models.storage_t == "db":
            __tablename__ = 'states'
            name = Column(String(128), nullable=False)
            cities = relationship("City", backref="state")
        else:
            name = ""

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)

        if models.storage_t != "db":
            @property
            def cities(self):
                """getter for list of city instances related to the state"""
                city_list = []
                all_cities = models.storage.all(City)
                for city in all_cities.values():
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
