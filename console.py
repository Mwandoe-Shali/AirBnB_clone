#!/usr/bin/python3

"""
this the command interpreter entry point
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        ''' method to exit command interpreter '''

        return True

    def do_EOF(self, line):
        ''' handles EOF to exit the command interpreter '''
        return True

    def emptyline(self):
        ''' overrides default emptyline execution '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
