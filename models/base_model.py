#!/usr/bin/python3
"""Base Model"""
from datetime import datetime
import uuid


class BaseModel():
    """defines all common attributes/methods for other classes""" 
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel"""
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return String Representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """update the the update_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dict_cp = self.__dict__.copy()

        dict_cp["__class__"] = self.__class__.__name__
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()

        return dict_cp
