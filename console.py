#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models import storage

cls_lst = ["BaseModel", "User", "State", "Amenity", "Place", "Review", "City"]
doc_ = "file.json"


class HBNBCommand(cmd.Cmd):
    """
    Your command interpreter should implement: quit and EOF to exit the prog
    help (this action is provided by default by cmd but you should keep it
    updated and documented) a custom prompt:
    (hbnb) an empty line + ENTER shouldn’t execute anything.
    Your code should not be executed when imported
    """

    """ I. documented functions: """

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_create(self, args):
        """
        Usage: $ create <model name>   ex: $ create BaseModel
        ---
        Creates a new instance of BaseModel, saves it (to the JSON file
        "filestorage") and prints the id
        If the class name is missing, prints ** class name missing **
        (ex: $ create).
        If the class name doesn’t exist, prints ** class
        doesn't exist ** (ex: $ create MyModel)
        """

        args = args.split(" ")

        if args[0] is None:
            print("** class name missing **")
        else:
            new_class_instance = None
            if (args[0] in cls_lst):
                new_class_instance = eval(args[0])()
                print(new_class_instance.id)
                new_class_instance.save()

        if new_class_instance is None:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Usage: $ all <Model name> or $ all      Ex: $ all BaseModel or $ all
        ---
        Prints all string representation of all instances based or not on the
        class name.
        The printed result is a list of strings
        If the class name doesn’t exist, prints ** class doesn't exist **
        (ex: $ all MyModel)
        """

        args = args.split(" ")
        dict_insts = storage.all()

        print(args, len(args))

        if (args[0] == ''):
            for key in dict_insts.keys():
                print(dict_insts[key])
        else:
            if (len(args) == 1 and args[0] not in cls_lst):
                print("** class doesn't exist **")
            else:
                for str_key in dict_insts.keys():
                    tokens = str_key.split(".")
                    if (tokens[0] == args[0]):
                        print(dict_insts[str_key])

    def do_show(self, args):
        """
        Usage: $ show <model name> <id>  ex: $ show BaseModel 1234-1234-1234.
        ---
        Prints the string rep of an instance based on the class name and id.
        If the class name is missing, prints ** class name missing **
        (ex: $ show).
        If the class name doesn’t exist, prints ** class doesn't exist **
        (ex: $ show MyModel).
        If the id is missing, prints ** instance id missing **
        (ex: $ show BaseModel).
        If the instance of the class name doesn’t exist for the id, prints
        ** no instance found ** (ex: $ show BaseModel 121212)
        """

        args = args.split(" ")

        if (len(args) == 0):
            print("** class name missing **")
        else:
            if (args[0] not in cls_lst):
                print("** class doesn't exist **")
            else:
                if (len(args) == 1 and args[0] in cls_lst):
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    dict_insts = storage.all()

                    if (key not in dict_insts):
                        print("** no instance found **")
                    else:
                        print(dict_insts[key])

    """ II. helper functions: """
    def emptyline(self):
        """Repeat last empty line & clean the buffer"""
        pass

if __name__ == '__main__':
    cmd = HBNBCommand()
    cmd.prompt = '(hbnb) '
    cmd.cmdloop()
