#!/usr/bin/python3
"""
Base model module.
Contains the BaseModel class that defines all common attributes/methods
                        for other classes.
"""

import uuid
from datetime import datetime

class BaseModel():
    """BaseModel class to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
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
        """Return string representation"""
        # type(self).__name__ == self.__class__.__name__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dict representation of instance"""
        # self.created_at.isoformat() == dict_cpy["created_at"].isoformat()
        dict_cpy = dict(self.__dict__)
        dict_cpy["__class__"] = type(self).__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        return dict_cpy