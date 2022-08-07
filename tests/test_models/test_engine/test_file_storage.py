#!/usr/bin/env python3
"""Test for file_storage"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models.user import User


class FileStorageTest(unittest.TestCase):
    """File_storage test"""
    def saveUser:
        new_model = BaseModel()
        new_model.name = "My_first"
        new_model.save
        all_obj = storage.all()
        for obj in all_obj.keys():
            del all_obj[obj]
        all_obj = storage.all()
        self.assertIsEqual(new_model, all_obj)
