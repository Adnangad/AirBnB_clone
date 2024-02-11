#!/usr/bin/python3
"""
This module contains a test class.
"""
from models.place import Place
from models import storage
from models.engine.file_storage import FileStorage
import unittest
import os


class TestPlace(unittest.TestCase):
    """
    This class tests the class Place.
    """
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_attributes(self):
        """This tests if the attributes are present"""
        a = Place()
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "description"))
        self.assertTrue(hasattr(a, "number_rooms"))
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertTrue(hasattr(a, "latitude"))
        self.assertTrue(hasattr(a, "longitude"))
        self.assertTrue(hasattr(a, "city_id"))

    def test_attr_empty(self):
        """This tests if at first the attr are empty strings"""
        a = Place()
        self.assertEqual(a.name, "")
        self.assertEqual(a.description, "")
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.city_id, "")

    def test_attributes(self):
        """This tests if the instances of attr."""
        a = Place()
        self.assertIsInstance(a, Place)
        self.assertIsInstance(a.name, str)
        self.assertIsInstance(a.longitude, float)
        self.assertIsInstance(a.max_guest, int)

    def test_custom_attr(self):
        """This tests the init of custom attr."""
        a = Place()
        a.location = "City"
        self.assertIn("location", a.to_dict())
        self.assertEqual(a.location, "City")

    def test_inherited_methods(self):
        """This tests methods like update, save etc"""
        a = Place()
        t = a.updated_at
        a.save()
        self.assertNotEqual(t, a.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method in Place if present."""
        a = Place()
        self.assertIn("created_at", a.to_dict())
        self.assertIn("updated_at", a.to_dict())

    def test_save_method(self):
        """
        This tests if the Place object can be written to a file.
        """
        a = Place()
        a.save()
        aid = "Place." + a.id
        with open("file.json", "r") as f:
            self.assertIn(aid, f.read())


if __name__ == '__main__':
    unittest.main()
