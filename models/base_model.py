#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        

    def __str__(self):
        # type(self).__name__ == self.__class__.__name__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        cp_dct = dict(self.__dict__)
        cp_dct["__class__"] = type(self).__name__
        cp_dct["created_at"] = self.created_at.isoformat()
        cp_dct["updated_at"] = self.updated_at.isoformat()
        return cp_dct