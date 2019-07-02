#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models.user import User
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
        Usage: $ create <Class name>
           Ex: $ create BaseModel
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

                print(args[0])

                new_class_instance = eval(args[0])()
                print(new_class_instance.id)
                new_class_instance.save()

        if new_class_instance is None:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Usage: $ all <Class Name> or $ all
           Ex: $ all BaseModel
           Ex: $ all
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
            i = 0
            for key in dict_insts.keys():
                print(dict_insts[key])
                print(i)
                i += 1
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
        Usage: $ show <Class name> <id>
           Ex: $ show BaseModel 1234-1234-1234.
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

    def do_destroy(self, args):
        """
        Usage: $ destroy <Class Name> <id>
           Ex: $ destroy BaseModel 1234
        ---
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        If the class name is missing, prints ** class name missing **
        (ex: $ destroy)
        If the class name doesn’t exist, prints ** class doesn't exist **
        (ex:$ destroy MyModel)
        If the id is missing, prints ** instance id missing **
        (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, prints
        ** no instance found ** (ex: $ destroy BaseModel 121212)
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
                        dict_insts.pop(key)
                        storage.save()

    def do_update(self, args):
        """
        Usage: $ update <Class name> <id> <attribute name> "<attribute value>"
           Ex: $ update BaseModel 1234 email "aibnb@holbertonschool.com"
        ---
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Only one attribute can be updated at the time.
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type

        If the class name is missing, prints ** class name missing **
        (ex: $ update)
        If the class name doesn’t exist, prints ** class doesn't exist **
        (ex: $ update MyModel)
        If the id is missing, prints ** instance id missing **
        (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id, prints
        ** no instance found **
        (ex: $ update BaseModel 121212)
        If the attribute name is missing, prints ** attribute name missing **
        (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, prints ** value
        missing ** (ex: $ update BaseModel existing-id first_name)
        All other arguments should not be used
        (Ex: $ update BaseModel 1234-1234 email "aibnb@holbertonschool.com"
        first_name "Betty" = $ update BaseModel 1234 email "aibnb@hs.com")
        id, created_at and updated_at cant’ be updated.
        """

    """ II. helper functions: """
    def emptyline(self):
        """Repeat last empty line & clean the buffer"""
        pass

if __name__ == '__main__':
    cmd = HBNBCommand()
    cmd.prompt = '(hbnb) '
    cmd.cmdloop()
