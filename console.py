#!/usr/bin/python3
"""
This is a cmd line interprator.
"""
import cmd
from models.base_model import BaseModel
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __inputs = ["BaseModel"]

    def do_quit(self, args):
        """Qiut command to exit the programm"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the programm"""
        print()
        return True

    def do_emptyline(self, args):
        """Handles empty lines."""
        pass

    def do_create(self, args):
        """Creates new instance of BaseModel, saves it and prints id"""
        if args is None or args == '':
            print("** class name missing **")
        else:
            if args not in HBNBCommand.__inputs:
                print("** class doesn't exist **")
            else:
                obj = eval(args)()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """Prints string rep of an instance based on class name and id"""
        if args is None or args == '':
            print("** class name missing **")
        else:
            word = args.split()
            if word[0] not in HBNBCommand.__inputs:
                print("** class doesn't exist **")
            elif word[1] is None or word[1] == '':
                print("** instance id missing **")
            else:
                k = f"{word[0]}.{word[1]}"
                if k in storage.all():
                    print(storage.all()[k])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args is None or args == '':
            print("** class name missing **")
        else:
            word = args.split()
            if word[0] not in HBNBCommand.__inputs:
                print("** class doesn't exist **")
            elif word[1] is None or word[1] == '':
                print("** instance id missing **")
            else:
                k = f"{word[0]}.{word[1]}"
                if k in storage.all():
                    del storage.all()[k]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """Prints string rep of all inst based or not on class name"""
        if args is None or args == '':
            for i in storage.all().values():
                print(i)
        else:
            if args not in HBNBCommand.__inputs:
                print("** class doesn't exist **")
            else:
                for k in storage.all().values():
                    if k.__class__.__name__ == args:
                        print(k)

    def do_update(self, args):
        """Updates inst based on clas name, id by adding or updating attr"""
        if args is None or args == '':
            print("** class name missing **")
        else:
            word = args.split()
            if word[0] not in HBNBCommand.__inputs:
                print("** class doesn't exist **")
            elif word[1] is None or word[1] == '':
                print("** instance id missing **")
            elif word[2] is None or word[2] == '':
                print("** attribute name missing **")
            elif word[3] is None or word[3] == '':
                print("** value missing **")
            else:
                if '"' in word[3]:
                    word[3] = word[3].replace('"', '')
                if re.search('^[0-9]', word[3]):
                    if '.' in word[3]:
                        word[3] = float(word[3])
                    else:
                        word[3] = int(word[3])
                k = f"{word[0]}.{word[1]}"
                c = storage.all()
                if k in c:
                    rez = c[k]
                    setattr(rez, word[2], word[3])
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
