#!/usr/bin/python3
"""
This is a cmd line interprator.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    this is usd to manipulate objects.
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        This cmd exits the prompt.
        """
        return True

    def do_EOF(self, args):
        """
        This cmd exits the prompt.
        """
        return True

    def do_emptyline(self, args):
        """Handles empty lines."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
