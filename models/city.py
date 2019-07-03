#!/usr/bin/python3
"""
module that define a class for the city
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
      state_id: string - empty string: it will be the State.id
      name: string - empty string
    """

    state_id = ""
    name = ""
