#!/usr/bin/python3
"""User Model"""


class User(BaseModel):
    """ a class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
