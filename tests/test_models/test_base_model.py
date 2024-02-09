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

    def test_kwargs(self):
        """This method tests the custom initialization."""
        custom_id = str(uuid.uuid4())
        custom_name = "Custom Name"
        custom_created_at = "2024-02-05T18:22:12.123456"
        custom_updated_at = "2024-02-05T18:22:12.123456"
        custom_number = 123
        obj = BaseModel(
                id=custom_id,
                name=custom_name,
                created_at=custom_created_at,
                updated_at=custom_updated_at,
                number=custom_number
                )
        self.assertEqual(obj.id, custom_id)
        self.assertEqual(obj.name, custom_name)
        self.assertEqual(
                obj.created_at,
                datetime.datetime.fromisoformat(custom_created_at))
        self.assertEqual(
                obj.updated_at,
                datetime.datetime.fromisoformat(custom_updated_at))
        self.assertEqual(obj.number, custom_number)
