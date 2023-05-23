#!/usr/bin/python3
""" Module test_base for unit testing """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_case(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

        with self.assertRaises(NameError):
            b6 = Base(Q)

        with self.assertRaises(TypeError):
            b7 = Base(1, 2)
