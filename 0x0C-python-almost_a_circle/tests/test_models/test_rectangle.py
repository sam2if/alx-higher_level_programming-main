#!/usr/bin/python3
""" Module test_base for unit testing """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        r1 = Rectangle(5, 7)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(6, 98)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(6, 4, 7, 3, 23)
        self.assertEqual(r3.id, 23)

        with self.assertRaises(TypeError):
            r4 = Rectangle(4, 7, 8, 9, 12, 2)

        with self.assertRaises(NameError):
            r5 = Rectangle(P, 8)

    def test_rectangle_validator(self):
        with self.assertRaises(TypeError) as e:
            r6 = Rectangle(7, "P")
        self.assertEqual("height must be an integer", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            rc = Rectangle("6", 7)
        self.assertEqual("width must be an integer", e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            rc1 = Rectangle(7, 9)
            rc1.width = -6
        self.assertEqual("width must be > 0", e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            rc1 = Rectangle(7, 9)
            rc1.height = -6
        self.assertEqual("height must be > 0", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            rc = Rectangle("6")
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            r7 = Rectangle(7, 9, -5, 7)
        self.assertEqual("x must be >= 0", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(5, 7)
            r8.x = {}
        self.assertEqual("x must be an integer", e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            r9 = Rectangle(10, 2, 3, -1)
        self.assertEqual("y must be >= 0", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            rt = Rectangle(10, 2, 3, 5)
            rt.y = []
        self.assertEqual("y must be an integer", e.exception.args[0])

        ra = Rectangle(4, 5, 6, 8, 9)
        self.assertEqual(ra.id, 9)

        rb = Rectangle(4, 5, 6, 8, 9)
        self.assertEqual(rb.width, 4)

        rc = Rectangle(4, 5, 6, 8, 9)
        self.assertEqual(rc.height, 5)

        rd = Rectangle(4, 5, 6, 8, 9)
        self.assertEqual(rd.x, 6)

        re = Rectangle(4, 5, 6, 8, 9)
        self.assertEqual(re.y, 8)

    def test_rectangle_area(self):
        rf = Rectangle(6, 5)
        self.assertEqual(rf.area(), 30)

        rh = Rectangle(10, 9, 0, 0, 12)
        self.assertEqual(rh.area(), 90)

        with self.assertRaises(TypeError):
            rx = Rectangle('X', 10)

        with self.assertRaises(ValueError):
            rs = Rectangle(0, -1)

    def test_rectangle_display(self):
        rq = Rectangle(5, 5)
        self.assertEqual(rq.width, 5)

        rk = Rectangle(4, 5, 6, 3)
        self.assertEqual(rk.x, 6)
        self.assertEqual(rk.y, 3)

    def test_rectangle_string(self):
        rh = Rectangle(5, 7, 3, 9, 12)
        self.assertEqual("[Rectangle] (12) 3/9 - 5/7", str(rh))

        rx = Rectangle(4, 3, 1, 0, 7)
        self.assertEqual("[Rectangle] (7) 1/0 - 4/3", str(rx))

    def test_rectangle_update(self):
        r12 = Rectangle(2, 4, 5, 6)
        r12.update(76)
        self.assertEqual("[Rectangle] (76) 5/6 - 2/4", str(r12))

        rr = Rectangle(6, 5, 7, 8)
        rr.update(6, 5, 8)
        self.assertEqual("[Rectangle] (6) 7/8 - 5/8", str(rr))

        rr.update(89, 6, 7, 56, 45)
        self.assertEqual("[Rectangle] (89) 56/45 - 6/7", str(rr))

        rm = Rectangle(20, 20, 20, 20, 89)
        rm.update(height=8)
        self.assertEqual("[Rectangle] (89) 20/20 - 20/8",str(rm))

        rm.update(width=1, x=2)
        self.assertEqual("[Rectangle] (89) 2/20 - 1/8", str(rm))

if __name__ == "__main__":
    unittest.main()
