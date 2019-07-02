#!/usr/bin/python3

from .base_model import BaseModel
"""
module that define a class for the user
"""


class User(BaseModel):
    """
    User class, class that define users
    """

    def __init__(self, *args, **kwargs):
        """
        public class atribute email, password first_name
        last_name
        """
        email = ""
        pasword = ""
        first_name = ""
        last_name = ""
        BaseModel.__init__(self, *args, **kwargs)
