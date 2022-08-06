#!/usr/bin/env python3
"""Module that defines the class FileStorage"""
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        if obj is not None:
            value = obj.to_dict()
            key = f"{value['__class__']}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_save = {}
        for key in self.__objects.keys():
            value = self.__objects[key].to_dict()
            dict_save[key] = value
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(dict_save, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from ..base_model import BaseModel
        from ..user import User
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                self.__objects = json.load(f)
            for key in self.__objects.keys():
                value = self.__objects[key]
                if key.startswith('BaseModel'):
                    self.__objects[key] = BaseModel(**value)
                elif key.startswith('User'):
                    self.__objects[key] = User(**value)
        except Exception:
            pass
