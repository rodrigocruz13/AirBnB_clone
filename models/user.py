#!/usr/bin/python3

from .base_model import BaseModel
"""
module that define a class for the user
"""


class User(BaseModel):
    """
    User class, class that define users
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
