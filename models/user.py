#!/usr/bin/python3
"""
module for user class
"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
