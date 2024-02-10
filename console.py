#!/usr/bin/python3
"""
This is a cmd line interprator.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    this is usd to manipulate objects.
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
