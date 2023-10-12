#!/usr/bin/python3
"""
This module can serialize instance to a JSON file and deserialize
JSON files back into instances.
"""
import json

"""Define a class FileStorage"""


class FileStorage:
    """class=-level attributes to store file path and objects."""
    __file_path = "file.json"
    __objects = {}
    # Define the 'models' dictionary to store class references.
    models = {}

    def all(self):
        """Retrieves all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize and save objects to a JSON file."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize objects from the JSON file and populate the storage."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = FileStorage.models.get(class_name)
                    if cls:
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
