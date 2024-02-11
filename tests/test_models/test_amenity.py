#!/usr/bin/python3
"""
This module contains a test class.
"""
from models.amenity import Amenity
from models import storage
from models.engine.file_storage import FileStorage
import unittest
import os


class TestAmenity(unittest.TestCase):
    """
    This class tests the class State.
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
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")

    def test_custom_attr(self):
        """Tests the creation of custom attr."""
        a = Amenity()
        a.year = 2024
        self.assertIn("year", a.to_dict())
        self.assertEqual(a.year, 2024)

    def test_save(self):
        """Tests the saving of place object to file."""
        a = Amenity()
        a.save()
        aid = "Amenity." + a.id
        with open("file.json", "r") as f:
            self.assertIn(aid, f.read())

    def test_inherited_attr(self):
        """Tests the inherited attr."""
        a = Amenity()
        b = a.updated_at
        a.save()
        self.assertIn("updated_at", a.to_dict())
        self.assertIn("created_at", a.to_dict())
        self.assertNotEqual(b, a.updated_at)


if __name__ == '__main__':
    unittest.main()
