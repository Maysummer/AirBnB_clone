#!/usr/bin/env python3
"""Test for file_storage"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorageTest(unittest.TestCase):
    """File_storage test"""

    def test_saveModel(self):
        model = BaseModel()
        model.name = "My_first"
        model.save()
        storage.all().clear()
        storage.reload()
        new_model = storage.all()[f'BaseModel.{model.id}']
        self.assertEqual(new_model.to_dict(), model.to_dict())


if __name__ == '__main__':
    unittest.main()
