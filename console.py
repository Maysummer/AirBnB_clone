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
        """Quit command to exit the program
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
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            base.save()
            print(base.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        if arg == "":
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                val = f"{word[0]}.{word[1]}"
                if val not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[val])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
