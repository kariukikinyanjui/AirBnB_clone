#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str) = email of the user
        password (str) = password of the user
        first_name (str) = first name of user
        last_name (str) = last name of user

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
