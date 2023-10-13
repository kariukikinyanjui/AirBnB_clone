#!/usr/bin/python3
"""
This module can serialize instance to a JSON file and deserialize
JSON files back into instances.
"""
import json
from models.base_model import BaseModel

"""Define a class FileStorage"""


class FileStorage:
    """class=-level attributes to store file path and objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieves all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serialize and save objects to a JSON file."""
        data = FileStorage.__objects
        data = {obj: data[obj].to_dict() for obj in data.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize objects from the JSON file and populate the storage."""
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for d in data.values():
                    cls_name = d["__class__"]
                    del d["__class__"]
                    self.new(eval(cls_name)(**d))
        except FileNotFoundError:
            return
