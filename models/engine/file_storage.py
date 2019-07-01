#!/usr/bin/python3
import json
import os.path
from ..base_model import BaseModel

""" the module that storage instances to a json files"""


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
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'a') as fileJ:
            dictionary = to_dict(FileSrotage.objects)
            json.dump(FileStorage.__objects, fileJ)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fileJ:
                __objects = json.load(fileJ)
        else:
            pass
