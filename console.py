#!/usr/bin/python3

"""
this the command interpreter entry point
"""
import sys
import cmd
import models
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "
    classes = ['User', 'City', 'State', 'Place',
               'Amenity', 'Review', 'BaseModel']

    def do_quit(self, args):
        ''' method to exit command interpreter '''

        return True

    def do_EOF(self, args):
        ''' handles EOF to exit the command interpreter '''
        return True

    def emptyline(self):
        ''' overrides default emptyline execution '''
        pass

    def do_create(self, args):
        ''' creates a new BaseMosel instance, saves it and
        prints the id '''
        createArgs = args.split()

        # missing class name condition
        if len(createArgs) == 0:
            print('** class name missing **')
        # non exixtant class name condition
        elif createArgs[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            cName = createArgs[0]
            # method returns a dict containing all global variables
            # and their values
            oClass = globals()[cName]
            ob = oClass()
            ob.save()
            print(ob.id)

    def do_update(self, args):
        ''' method updates an instance based on class name and id
        by adding or updating attributes, saving changes to the JSON file '''
        updateArgs = args.split()
        obStored = models.storage.all()

        if len(updateArgs) == 0:
            print('** class name missing **')
        elif updateArgs[0] not in self.classes:
            print("** class doesn't exist **")
            # missing id condition
        elif len(updateArgs) < 2:
            print('** instance id missing **')
        else:
            cName = updateArgs
            uid = updateArgs[1]
            obKey = f'{cName}.{uid}'

            # class name instance doesn't exist for the id
            if obKey not in obStored.keys():
                print('** no instance found **')
            # missing attribute name
            elif len(updateArgs) < 3:
                print('** attribute name missing **')
            # non-existant attribute name value
            elif len(updateArgs) < 4:
                print('** value missing **')
            else:
                atrName = updateArgs[2]
                atrValue = updateArgs[3]
                ob = obStored.get(obKey)

                if atrName in ob.__dict__.keys():
                    valueType = type(ob.__dict__.get(atrName))
                    ob.__dict__[atrName] = valueType(atrValue)
                else:
                    ob.__dict__[atrName] = atrValue

                ob.save()

    def do_show(self, args):
        ''' method prints str representation of an instance based
        on the class name and id'''
        showArgs = args.split()

        # missing class name
        if len(showArgs) == 0:
            print('** class name missing **')
        # non-existant class name
        elif showArgs[0] not in self.classes:
            print("** class doesn't exist **")
        # missing id
        elif len(showArgs) < 2:
            print('** instance id missing **')
        else:
            cName = showArgs[0]
            uid = showArgs[1]
            obKey = f'{cName}.{uid}'

            # class name instance doesn't exist for the id
            if obKey not in models.storage.all().keys():
                print('** no instance found **')
            else:
                ob = models.storage.all().get(obKey)
                print(ob)

    def do_destroy(self, args):
        ''' method deletes an instance based on the class name and id'''
        destroyArgs = args.split()

        # missing class name
        if len(destroyArgs) == 0:
            print('** class name missing **')
        # class name don't exist
        elif destroyArgs[0] not in self.classes:
            print("** class doesn't exist **")
        # missing id
        elif len(destroyArgs) < 2:
            print('** no instance found **')
        else:
            cName = destroyArgs[0]
            uid = destroyArgs[1]
            obKey = f'{cName}.{uid}'

            if obKey not in models.storage.all().keys():
                print('** no instance found **')
            else:
                obStored = models.storage.all()
                obStored.pop(obKey)
                models.storage.save()

    def do_all(self, args):
        ''' method prints all str representation of all
        instances based or not on the class name'''
        allArgs = args.split()
        obStored = models.storage.all()
        printAll = []

        if len(allArgs) == 0:
            for obKey in obStored.keys():
                ob = obStored.get(obKey)
                printAll.insert(0, ob.__str__())
            print(printAll)
        else:
            # class name don't exist
            if allArgs[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                cName = allArgs[0]
                for obKey in obStored.keys():
                    # returns True if the str starts with class name
                    if obKey.startswith(cName):
                        ob = obStored.get(obKey)
                        printAll.insert(0, obj.__str__())
                print(printAll)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
