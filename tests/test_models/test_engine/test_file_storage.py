#!/usr/bin/python3
"""
This is a test Module
"""
from models.engine.file_storage import FileStorage
import json
import os
from models import storage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """
    This class tests the FileStorage class.
    """
    def setUp(self):
        """
        This sets up some variable that we'll use.
        """
        self.storage = FileStorage()
        self.file_path = "file.json"

    def tearDown(self):
        """
        Removes the file.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """
        Tests the all, new and save methods.
        """
        new_obj = BaseModel()
        new_obj.id = "new_id"
        self.storage.new(new_obj)
        self.assertIn("BaseModel.new_id", self.storage._FileStorage__objects)

    def test_all(self):
        """
        Tests the all method.
        """
        new_obj = BaseModel()
        new_obj.id = "test_id"
        new_obj.name = "test_name"
        self.storage.new(new_obj)
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn("BaseModel.test_id", all_objects)

    def test_save_reload(self):
        """
        Tests the save and reload method.
        """
        new_obj = BaseModel()
        new_obj.id = "test_id"
        new_obj.name = "test_name"
        self.storage.new(new_obj)
        self.storage.save()

        reloaded_storage = FileStorage()
        reloaded_storage.reload()

        reloaded_objects = reloaded_storage.all()
        reloaded_obj = reloaded_objects["BaseModel.test_id"]
        self.assertEqual(reloaded_obj.name, "test_name")

    def test_save_reload_json(self):
        """
        tests the writing and reading in files.
        """
        new_obj = BaseModel()
        new_obj.id = "test_id"
        new_obj.name = "test_name"
        self.storage.new(new_obj)
        self.storage.save()

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.assertIn("BaseModel.test_id", data)
        self.assertEqual(data["BaseModel.test_id"]["name"], "test_name")


if __name__ == '__main__':
    unittest.main()
