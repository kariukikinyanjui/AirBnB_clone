#!/usr/bin/python
"""Defines a class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A simple model of reviews.

    Attributes:
        place_id (str): Place ID
        user_id (str): User ID
        text (str): text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
