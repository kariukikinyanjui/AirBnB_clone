#!/usr/bin/python3
"""Defines the class State."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Simple model of a state.

    Attributes:
        name (str): Name of the state.
    """

    name = ""
