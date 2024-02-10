#!/usr/bin/python3
"""
This module contains a test class.
"""
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage
import unittest
import os


class TestUser(unittest.TestCase):
    """
    This class tests the class User.
    """
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_attributes(self):
        """This tests if the attributes are present"""
        a = User()
        self.assertTrue(hasattr(a, "email"))
        self.assertTrue(hasattr(a, "password"))
        self.assertTrue(hasattr(a, "first_name"))
        self.assertTrue(hasattr(a, "last_name"))

    def test_attr_empty(self):
        """This tests if at first the attr are empty strings"""
        a = User()
        self.assertEqual(a.email, "")
        self.assertEqual(a.password, "")
        self.assertEqual(a.last_name, "")
        self.assertEqual(a.first_name, "")

    def test_savereload_method(self):
        """
        This tests if the User object can be written to a file.
        """
        new_obj = User()
        new_obj.id = "test_id"
        new_obj.first_name = "test_name"
        self.storage.new(new_obj)
        self.storage.save()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        reloaded_objects = reloaded_storage.all()
        reloaded_obj = reloaded_objects["BaseModel.test_id"]
        self.assertEqual(reloaded_obj.name, "test_name")


if __name__ == '__main__':
    unittest.main()
