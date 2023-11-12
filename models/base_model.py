#!/usr/bin/python3
"""
Base model module.
Contains the BaseModel class that defines all common attributes/methods
                        for other classes.
"""

import uuid
from datetime import datetime

class BaseModel():
    """BaseModel class to inherit from.
    Initializes public instance attributes:
    - id: string - assign with an uuid when an instance is created
    - created_at: datetime - assign with the current datetime when an instance is created
    - updated_at: datetime - assign with the current datetime when an instance is created and
                                                it will be updated every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            args (any): Unused.
            kwargs (dict): Key/value pairs of attributes.
        """
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
        """Return string representation.
        Shows class name, id, and dictionary representation.
        """
        # type(self).__name__ == self.__class__.__name__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return the dictionary representation of the BaseModel.
        Includes ISO formatted datetime strings.
        """
        # self.created_at.isoformat() == dict_cpy["created_at"].isoformat()
        dict_cpy = dict(self.__dict__)
        dict_cpy["__class__"] = type(self).__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        return dict_cpy