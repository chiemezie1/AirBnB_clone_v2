#!/usr/bin/python3
"""

Module defining BaseModel class.

"""

import uuid

from datetime import datetime
import models


class BaseModel:
    """
    BaseModel Class that defines all common
        attributes/methods for other classes

    Attributes:
        id (str): unique UUID for each instance
        created_at (datetime): instance creation datetime
        updated_at (datetime): instance update datetime
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method

        Args:
            *args: variable length argument list
            **kwargs: variable length keyword argument list
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel instance in format:
                [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: BaseModel instance representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
                updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict ionary containing all
                keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
