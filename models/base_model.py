#!/usr/bin/python3

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
