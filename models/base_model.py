#!/usr/bin/python3
"""Base Model"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """defines all common attributes/methods for other classes""" 

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel"""
        date_formate = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if args is not None and len(args) > 0:
            pass
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_formate)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return String Representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """update the the update_at"""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dict_cp =self.__dict__.copy() 

        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        dict_cp["__class__"] = self.__class__.__name__

        return dict_cp
