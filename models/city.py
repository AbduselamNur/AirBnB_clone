#!/usr/bin/python3
"""city Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class that inherit from BaseModel"""
    state_id = ""
    name = ""
