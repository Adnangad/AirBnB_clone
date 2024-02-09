#!/usr/bin/python3
"""
This module tests the BaseModel class
"""
import unittest
import datetime
from models.base_model import BaseModel
import os
import uuid


class TestBaseModel(unittest.TestCase):
    """
    This class tests the BaseModel.
    """
    def test_init(self):
        """
        This method tests the initialization of attributes.
        """
        a = BaseModel()
        b = BaseModel()
        self.assertTrue(hasattr(a, "id"))
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertNotEqual(b.id, a.id)
        self.assertIsInstance(b.id, str)
        c = a.created_at
        self.assertIsInstance(c, datetime.datetime)

    def test_save(self):
        """
        This method tests the method save.
        """
        a = BaseModel()
        b = a.updated_at
        a.save()
        self.assertNotEqual(b, a.updated_at)

    def test_str(self):
        """
        This method test the __str__ method.
        """
        a = BaseModel()
        rep = str(a)
        nm = a.__class__.__name__
        self.assertIn(f"[{nm}]", rep)
        self.assertIn(f"({a.id})", rep)

    def test_todict(self):
        """This method tests the to_dict method."""
        a = BaseModel()
        c = a.to_dict()
        self.assertIsInstance(c, dict)
        self.assertIn("created_at", c)
        self.assertIn("__class__", c)
        self.assertEqual(c["__class__"], "BaseModel")
        self.assertIn("updated_at", c)
        self.assertEqual(c["created_at"], a.created_at.isoformat())
        self.assertEqual(c["updated_at"], a.updated_at.isoformat())
