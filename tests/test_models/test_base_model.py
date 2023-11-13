#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        
    def test_uuid(self):
        """Test id is a valid uuid"""
        model = BaseModel()
        self.assertIs(type(model.id), str)

    def test_datetime(self):
        """Test created_at and updated_at are datetime objects"""
        model = BaseModel() 
        self.assertIs(type(model.created_at), datetime)
        self.assertIs(type(model.updated_at), datetime)

    def test_str(self):
        """Test __str__ representation"""
        model = BaseModel()
        dt = datetime.today()  
        model.id = "12345"
        model.created_at = dt
        model.updated_at = dt
        expect = "[BaseModel] (12345) {}".format(model.__dict__)
        self.assertEqual(str(model), expect)

    def test_save(self):
        """Test save updates updated_at""" 
        model = BaseModel()
        old_update = model.updated_at
        model.save()
        self.assertNotEqual(old_update, model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        d = model.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

if __name__ == "__main__":
    unittest.main()