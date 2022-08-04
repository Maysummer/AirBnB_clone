#!/usr/bin/env python3
"""program that contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class for interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """do nothing if ENTER is pressed"""
        return False

    def default(self, line):
        """exit the program"""
        if line == 'EOF':
            return True
        return super().default(line)

    """def do_help(self, arg):
        print(arg)"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
