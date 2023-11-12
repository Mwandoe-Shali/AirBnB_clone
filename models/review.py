#!/usr/bin/python3
""""Defines the Review class.
Inherits from BaseModel class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""