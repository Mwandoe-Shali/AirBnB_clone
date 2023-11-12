#!/usr/bin/python3
<<<<<<< HEAD

'''
BaseModel class definition module
'''

from datetime import datetime
import models
import json
import uuid


class BaseModel:
    '''
    class defines all common attributes or methods for
    other classes
    '''

    def __init__(self, *var, **kars):
        """
        method instantiates BaseModel attributes, takes two args(var and kvars)
        vars - allows passing of an unpredictable args number
        kars - a dictionary, allows handling named args not mentioned
        in advance, has attributes three attributes(id, created_at, updated_at)
        id - a str represeting a new instance unique id,
        created_at - datetime the object was created
        updated_at - datetime object was updated
        """

        if kars and len(kars) > 0:
            for qi in kars.keys():
                if type(qi) is str and qi != '__class__':
                    if qi == 'updated_at' or qi == 'created_at':
                        kars[qi] - datetime.fromisoformat(kars[qi])
                    self.__dict__[qi] = kars[qi]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        method returns BaseModel class string representation
        '''

        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        '''
        method updates public instance attribute (updated_at) with the
        current datetime
        '''

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
        method returns a dict containing all keys/values of instance __dict__
        '''

        myDict = self.__dict__.copy()
        myDict['__class__'] = type(self).__name__
        myDict['updated_at'] = myDict['updated_at'].isoformat()
        myDict['created_at'] = myDict['created_at'].isoformat()
        return myDict
=======
"""
Base model module.
Contains the BaseModel class that defines all common attributes/methods
                        for other classes.
"""

from uuid import uuid4
from datetime import datetime
from models import storage

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
                elif key == "__class__":
                    setattr(self, key, type(self))
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation.
        Shows class name, id, and dictionary representation.
        """
        # type(self).__name__ == self.__class__.__name__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with current time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

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
>>>>>>> c447bbc3bfc2d4f3bd5ebb750d8d98b2fa802cd4
