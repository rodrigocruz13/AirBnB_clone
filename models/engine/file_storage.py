#!/usr/bin/python3
""" the module that storage instances to a json files"""
import json
import os.path
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage():
    """
    Class that serializes instances to a JSON files and
    deserializes JSON file to instances
    arributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id
               (ex: to store a BaseModel object with id=12121212, the key will
               be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        o = obj
        FileStorage.__objects[o.__class__.__name__ + "." + o.id] = o

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = {}
        with open(FileStorage.__file_path, 'w') as fileJ:
            for dic in FileStorage.__objects:
                dictionary[dic] = BaseModel.to_dict(FileStorage.__objects[dic])
            json.dump(dictionary, fileJ)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        classes = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
        if os.path.exists(FileStorage.__file_path):
            dictionary = {}
            with open(FileStorage.__file_path, 'r') as fileJ:
                dictionary = json.load(fileJ)
            for dic, value in dictionary.items():
                nameClass = dic.split(".")[0]
                for clase in classes:
                    if nameClass == clase:
                        FileStorage.__objects[dic] = eval(nameClass)(**value)
                        break
        else:
            pass
