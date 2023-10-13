#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Contains entry point of the command interpreter
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]

    def do_quit(self, args):
        """Quit command to exit the programm"""
        return True

    def do_EOF(self, args):
        """End Of File command to exit the programm"""
        return True

    def emptyline(self):
        """Do nothing when executing an empty line"""
        pass

    @classmethod
    def verify_class(cls, line):
        """Class method to verify inputed class"""
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class_name>
        Ex: $ create BaseModel
        """
        line = args.split()
        if not self.verify_class(line):
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    @staticmethod
    def verify_id(line):
        """Static method to verify for id"""
        if len(line) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        key = f"{line[0]}.{line[1]}"

        if key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class
        name and id
        Usage: show <class_name> <id>
        Ex: $ show BaseModel 1234-1234-1234
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        objects = models.storage.all()
        key = f"{line[0]}.{line[1]}"
        print(objects[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class_name> <id>
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        objects = models.storage.all()
        key = f"{line[0]}.{line[1]}"
        del objects[key]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation af all instances based or not on the
        class name
        Usage: all <class_name> OR all
        Ex: $ all BaseModel OR $ all
        """
        line = args.split()
        objects = models.storage.all()
        if len(line) == 0:
            for v in objects.values():
                print(str(v))
        elif line[0] in HBNBCommand.class_list:
            for k, v in objects.items():
                print(str(v))
        else:
            print("** class doesn't exist **")
            return False

    @staticmethod
    def verify_attribute(line):
        """Static method to verify attributes in line input"""
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        Usage: update <class_name> <id> <attribute name> <attribute value>
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = models.storage.all()
        key = f"{line[0]}.{line[1]}"
        setattr(objects[key], line[2], line[3])
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
