#!/usr/bin/python3
"""module for review"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """the class review"""

    place_id = ""
    user_id = ""
    text = ""
