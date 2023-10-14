#!/usr/bin/python3
"""
This module contains unit tests for BaseModel
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class that tests for BaseModel"""
    def test_attributes(self):
        """
        Tests for the attributes used in initializing the BaseModel class
        """
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_id_assignment(self):
        """Tests for uniqueness of id assignment"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_datetime(self):
        """Tests if created_at attribute is a datetime object type"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_datetime(self):
        """Tests if updated_at attribute is a datetime object type"""
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save(self):
        """Tests if save() method updates the update_at attribute"""
        instance = BaseModel()
        attr_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(attr_updated_at, instance.updated_at)

    def test_to_dict(self):
        """Tests for the to_dict() method if it really converts to a dict"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_str(self):
        """Tests for the str method if it returns a string representation"""
        instance = BaseModel()
        instance_str = str(instance)
        self.assertIsInstance(instance_str, str)
        self.assertTrue(instance.__class__.__name__ in instance_str)
        self.assertTrue(instance.id in instance_str)
        self.assertTrue(str(instance.__dict__) in instance_str)


if __name__ == "__main__":
    unittest.main()
