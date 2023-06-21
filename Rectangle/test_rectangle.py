#Unit tests for rectangle program

import unittest
from pydoc import *
from rectangle import Rectangle,Parallelepiped

#Unit Tests for Area, Perimeter and Volume

class TestRectangle(unittest.TestCase):
    width=4
    length=5
    height=2
    def test_Rectangle(self):
        self.assertEqual(Rectangle.Area(self),20)
        self.assertEqual(Rectangle.Perimeter(self),18)
        self.assertEqual(Parallelepiped.Volume(self),40)

if __name__ == '__main__':
    unittest.main()