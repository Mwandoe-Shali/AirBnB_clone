#!/usr/bin/python3

import datetime
import uuid

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs != {} and kwargs is not None:
            for arg in kwargs:
                if arg == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif arg == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[arg] = kwargs[arg]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        kamusi = self.__dict__.copy()
        kamusi["__class__"] = type(self).__name__
        kamusi["created_at"] = kamusi["created_at"].isoformat()
        kamusi["updated_at"] = kamusi["updated_at"].isoformat()
        return kamusi