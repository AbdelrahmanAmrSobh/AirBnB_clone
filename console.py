#!/usr/bin/python3
"""The console"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
        class_names = ["BaseModel", "User", "Place", "State",
                       "City", "Amenity", "Review"]
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
        class_name = HBNBCommand.check_class_name(line)
        if class_name is False:
            return
        if class_name == "BaseModel":
            new_i = BaseModel()
        elif class_name == "User":
            new_i = User()
        elif class_name == "Place":
            new_i = Place()
        elif class_name == "State":
            new_i = State()
        elif class_name == "City":
            new_i = City()
        elif class_name == "Amenity":
            new_i = Amenity()
        elif class_name == "Review":
            new_i = Review()
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

    def default(self, line):
        """
        allow the usage of class_name.function(parameters)
        Ex: $ BaseModel.all()
        Eq: $ all BaseModel
        """
        arguments = line.split('.')
        try:
            class_name = arguments[0]
            arguments = arguments[1].split('(')
            function_name = arguments[0]
            arguments = arguments[1].split(')')[0].split(', ')
        except IndexError:
            return cmd.Cmd().default(line)
        functions = {
                "all": self.do_all,
                "count": self.count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        if HBNBCommand.check_class_name(class_name) is False:
            return
        if function_name == "all":
            self.do_all(class_name)
        elif function_name == "count":
            self.count(class_name)
        elif function_name == "show":
            self.do_show(class_name + " " + arguments[0])
        elif function_name == "destroy":
            self.do_destroy(class_name + " " + arguments[0])
        elif function_name == "update":
            if len(arguments) == 3:
                self.do_update(class_name + " " + arguments[0] + " "
                               + arguments[1] + " " + arguments[2])
            else:
                pass

    def count(self, line):
        """
        retrieve the number of instances of a class
        """
        instances = 0
        storage.all()
        for key, value in storage.all().items():
            if key.split('.')[0] == line:
                instances += 1
        print(instances)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
