#!/usr/bin/python3

import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Class that serializes instances to a JSON file and
                deserializes JSON file to instances:
    i.e Class for storing and retrieving data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            dict_a = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict_a, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                for key, value in (json.load(file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
