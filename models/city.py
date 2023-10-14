#!/usr/bin/python3
"""Defines a class City."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Simple model of a city.

    Attributes:
        state_id (str): state of the city
        name (str): name of the city
    """
    state_id = ""
    name = ""
