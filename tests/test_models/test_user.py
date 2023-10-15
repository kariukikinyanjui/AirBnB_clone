#!/usr/bin/python3
"""
This module contains unit tests for User
"""
import unittest
from models.user import User
from datetime import datetime
import models


class TestUser(unittest.TestCase):
    """Class that tests for User"""
    def test_inheritance(self):
        """Tests if User inherits from the BaseModel class"""
        user = User()
        self.assertIsInstance(user, models.base_model.BaseModel)

    def test_attributes_exist(self):
        """
        Tests if all attributes, those inherited from BaseModel and those
        belonging to User exists
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_email_password_first_name_last_name(self):
        """Tests if attributes of user class are empty"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_email_password_first_name_last_name_types(self):
        """Tests if attributes for user class are of type string"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_to_dict_returns_dict(self):
        """Tests if to_dict method returns a dictionary of the user class"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)


if __name__ == '__main__':
    unittest.main()
