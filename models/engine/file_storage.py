#!/usr/bin/python3
"""

Module defining FileStorage class.

"""

import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage Class that serializes instances
        to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary of objects
    """

    def __init__(self):
        """Constructor method"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
