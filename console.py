#!/usr/bin/python3
"""The console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Controls the console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit of the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def check_class_name(line, prints=True):
        """
        checks a given name if exist and if valid
        """
        class_names = ["BaseModel"]
        arguments = line.split()
        if len(arguments) == 0:
            if prints:
                print("** class name missing **")
                return False
            return ""
        elif arguments[0] not in class_names:
            print("** class doesn't exist **")
            return False
        return arguments[0]

    def check_class_id(line):
        """
        checks if id is given and if so if its valid for given class
        """
        arguments = line.split()
        if len(arguments) < 2:
            print("** instance id missing **")
            return False
        given_id = arguments[0] + '.' + arguments[1]
        if given_id not in storage.all():
            print("** no instance found **")
            return False
        return given_id

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if HBNBCommand.check_class_name(line) is False:
            return
        new_i = BaseModel()
        new_i.save()
        print(new_i.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        if HBNBCommand.check_class_name(line) is False:
            return
        given_id = HBNBCommand.check_class_id(line)
        if given_id is False:
            return
        print(storage.all()[given_id])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if HBNBCommand.check_class_name(line) is False:
            return
        given_id = HBNBCommand.check_class_id(line)
        if given_id is False:
            return
        del storage.all()[given_id]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        class_name = HBNBCommand.check_class_name(line, False)
        if class_name is False:
            return
        match_list = []
        for key, value in storage.all().items():
            if class_name == "" or class_name == key.split('.')[0]:
                match_list.append(str(value))
        print(match_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        arguments = line.split()
        length = len(arguments)
        class_name = HBNBCommand.check_class_name(line)
        if class_name is False:
            return
        given_id = HBNBCommand.check_class_id(line)
        if given_id is False:
            return
        elif length == 2:
            print("** attribute name missing **")
            return
        elif length == 3:
            print("** value missing **")
            return
        setattr(storage.all()[given_id], arguments[2], arguments[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
