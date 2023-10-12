#!/usr/bin/python3
"""This module contains the entry point of the commad interpreter."""
import cmd

"""Define a class HBNBCommand."""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
