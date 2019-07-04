#!/usr/bin/python3
"""the unitest for BaseModel"""
import unittest
from models.base_model import BaseModel
import os
import pep8
from models import storage


class TestBaseModel(unittest.TestCase):
    """this class test the class BaseModel
    """

    @classmethod
    def setUpClass(cls):
        """
        set up the class before every test
        """
        cls.base1 = BaseModel()

    @classmethod
    def teardown(cls):
        """
        remove test instances
        """
        del cls.baseT
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        """Pep8 style test"""
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring(self):
        """
        Test if the model are documented
        """
        for documen in dir(BaseModel):
            self.assertIsNotNone(documen.__doc__)

    def test_docstrign_class(self):
        """
        Test if the classes are documented
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_method(self):
        """
        Test for the class have methods
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_has_atribute(self):
        """
        Test for the atributes of the instance
        """
        self.assertTrue('updated_at' in self.base1.__dict__)
        self.assertTrue('created_at' in self.base1.__dict__)
        self.assertTrue('id' in self.base1.__dict__)

    def test_has_instance(self):
        """
        Test if the instance exist in the class
        """
        self.assertIsInstance(self.base1, BaseModel)

    def test_save(self):
        """
        test for the save method
        """
        test = BaseModel()
        test_id = test.id
        test.name = "Miguel"
        test.save()
        BaseModel.save(test)
        storage.reload()
        objs = storage.all()
        my_objs = objs["BaseModel.{}".format(test_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Miguel")
        self.assertTrue(os.path.exists('file.json'))

    def test_dictionary(self):
        """
        test for the dictionary
        """
        dictionary_T = self.base1.to_dict()
        self.assertEqual(type(dictionary_T), dict)
        self.assertEqual(type(dictionary_T['updated_at']), str)
        self.assertEqual(type(dictionary_T['created_at']), str)
        self.assertTrue('__class__' in dictionary_T)


if __name__ == "__main__":
    unittest.main()
