#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """Manege file storage for object"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return Dectionary Object"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object to dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serilalizes object to json"""
        dict_json = {
                key: obj.to_dict() for key, obj in
                FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_json, f)

    def reload(self):
        """
        deserialization of Object"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name = value["__class__"]
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
