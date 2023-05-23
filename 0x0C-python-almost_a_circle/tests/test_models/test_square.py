#!/usr/bin/python3
""" Module test_base for unit testing """

import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):

    def test_square(self):
        s1 = Square(4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.area(), 16)

        s2 = Square(3, 3)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.area(), 9)

        s3 = Square(5, 2, 7)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s3.area(), 25)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 7)

    def test_square_size(self):
        s4 = Square(6)
        self.assertEqual("[Square] (4) 0/0 - 6", str(s4))

        with self.assertRaises(TypeError):
            s5 = Square("9")

    def test_square_update(self):
        s6 = Square(7)
        self.assertEqual("[Square] (6) 0/0 - 7",str(s6))

        s6.update(15)
        self.assertEqual("[Square] (15) 0/0 - 7",str(s6))

        s6.update(7, 9)
        self.assertEqual("[Square] (7) 0/0 - 9",str(s6))

        s6.update(size=56, id=45, y= 6)
        self.assertEqual("[Square] (45) 0/6 - 56",str(s6))

        s6.update(u=67)
        self.assertEqual("[Square] (45) 0/6 - 56",str(s6))
