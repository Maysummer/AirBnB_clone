#!/usr/bin/env python3
"""program that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Enter Ctrl+D to exit the program
        """
        # print is so that ctrl+d leaves a new line
        print()
        return True

    def emptyline(self):
        """do nothing if ENTER is pressed"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if self.verify_arg(arg, False):
            base = BaseModel()
            base.save()
            print(base.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        if self.verify_arg(arg, True):
            word = arg.split(' ')
            val = f"{word[0]}.{word[1]}"
            print(storage.all()[val])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if self.verify_arg(arg, True):
            word = arg.split(' ')
            val = f"{word[0]}.{word[1]}"
            del storage.all()[val]
            storage.save()


    def verify_arg(self, arg, idCheck):
        """Checks that arg to a command is correct"""
        if arg == "":
            print("** class name missing **")
            return False
        word = arg.split(' ')
        if word[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        if idCheck:
            if len(word) < 2:
                print("** instance id missing **")
                return False
            val = f"{word[0]}.{word[1]}"
            if val not in storage.all():
                print("** no instance found **")
                return False
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
