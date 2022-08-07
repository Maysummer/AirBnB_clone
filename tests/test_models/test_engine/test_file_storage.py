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
        """Test serialization and deserialization of
        BaseModel instance"""
        model = BaseModel()
        model.save()
        storage.all().clear()
        storage.reload()
        new_model = storage.all()[f'BaseModel.{model.id}']
        self.assertEqual(new_model.to_dict(), model.to_dict())

    def test_saveUser(self):
        """Test serialization and deserialization of
        User instance"""
        user = User()
        user.first_name = 'Ebube'
        user.last_name = 'Chukwuma'
        user.email = 'ebube@chukwuma.com'
        user.password = 'root'
        user.save()
        storage.all().clear()
        storage.reload()
        new_user = storage.all()[f'User.{user.id}']
        self.assertEqual(new_user.to_dict(), user.to_dict())

    def test_saveState(self):
        """Test serialization and deserialization of
        State instance"""
        state = State()
        state.name = 'Anambra'
        state.save()
        storage.all().clear()
        storage.reload()
        new_state = storage.all()[f'State.{state.id}']
        self.assertEqual(new_state.to_dict(), state.to_dict())

if __name__ == '__main__':
    unittest.main()
