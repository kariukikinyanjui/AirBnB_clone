#!/usr/bin/python3
"""
This module contains a class that defines all common attributes/methods
for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is the base class that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with public instance attributes

        Attributes:
        id: assigned with uuid to provide a unique id for each BaseModel
            instance created
        created_at: uses datetime to assign the current datetime when an
            instance is created
        updated_at: uses datetime to assign the current datetime when an
            instance is created & updated everytime the object is changed
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        Public instance method that updates the public instance attribute
        'updated_at' with the current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Public instance method that returns a dictionary ontaining all
        key/value pairs of __dict__ of the instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        return {
                key: value.isoformat() if isinstance(value, datetime)
                else value for key, value in dict_obj.items()
                }

    def __str__(self):
        """Returns the string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
