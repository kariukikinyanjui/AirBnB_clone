#!/usr/bin/python3
"""
This module contains unittest cases for FileStorage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from copy import deepcopy


class TestFileStorage(unittest.TestCase):
    """Class that tests for FileStorage"""
    @classmethod
    def setUpClass(cls):
        """method to create an instance of FileStorage"""
        cls.storage = FileStorage()
        cls.model = BaseModel()
        cls.storage.new(cls.model)
        cls.storage.save()

    @classmethod
    def tearDownClass(cls):
        """method to clean up after each test by removing the test file"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Tests for all() method of the FileStorage class"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      objects)

    def test_new(self):
        """Tests for new() method of the FileStorage class"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"{new_model.__class__.__name__}.{new_model.id}",
                      self.storage.all())

    def test_save(self):
        """Tests for save() method of the FileStorage class"""
        objects_initial = deepcopy(self.storage.all())
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        objects_after = deepcopy(self.storage.all())
        self.assertNotEqual(objects_initial, objects_after)

    def test_reload(self):
        """TEsts for reload() method of the FileStoraage class"""
        objects_initial = self.storage.all()
        self.storage.reload()
        objects_after = self.storage.all()
        self.assertEqual(objects_initial, objects_after)


if __name__ == "__main__":
    unittest.main()
