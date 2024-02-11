#!/usr/bin/python3
"""
This module contains a test class.
"""
from models.city import City
from models import storage
from models.engine.file_storage import FileStorage
import unittest
import os


class TestCity(unittest.TestCase):
    """
    This class tests the class City.
    """
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_attributes(self):
        """
        Tests the attr if present.
        """
        a = City()
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "state_id"))
        self.assertEqual(a.name, "")
        self.assertEqual(a.state_id, "")

    def test_custom_attr(self):
        """Tests the creation of custom attr."""
        a = City()
        a.year = 2024
        self.assertIn("year", a.to_dict())
        self.assertEqual(a.year, 2024)

    def test_save(self):
        """Tests the saving of place object to file."""
        a = City()
        a.save()
        aid = "City." + a.id
        with open("file.json", "r") as f:
            self.assertIn(aid, f.read())

    def test_inherited_attr(self):
        """Tests the inherited attr."""
        a = City()
        b = a.updated_at
        a.save()
        self.assertIn("updated_at", a.to_dict())
        self.assertIn("created_at", a.to_dict())
        self.assertNotEqual(b, a.updated_at)


if __name__ == '__main__':
    unittest.main()
