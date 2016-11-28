#kompilacja z python3

import unittest
from rectangle import *

class TestRectangle(unittest.TestCase):

    def setUp(self): pass
        
    def test_init_rect(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Rectangle(4,3,2,1)
        
    def test_str_rect(self):
        self.assertEqual(str(Rectangle(1,2,3,4)), "[(1, 2), (3, 4)]")
        
    def test_eq_rect(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Rectangle(4,3,2,1)
        self.assertTrue(Rectangle(1,2,3,4) == Rectangle(1,2,3,4))
        self.assertFalse(Rectangle(1,2,3,4) == Rectangle(1,2,6,7))
        
    def test_ne_rect(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Rectangle(4,3,2,1)
        self.assertFalse(Rectangle(1,2,3,4) != Rectangle(1,2,3,4))
        self.assertTrue(Rectangle(1,2,3,4) != Rectangle(1,2,6,7))
        
    def test_center(self):
        self.assertEqual(Rectangle(2,2,4,4).center(), Point(3,3))
        self.assertEqual(Rectangle(2,2,10,4).center(), Point(6,3))
        
    def test_area(self):
        self.assertEqual(Rectangle(2,2,4,4).area(), 4)
        self.assertEqual(Rectangle(2,2,10,4).area(), 16)
        
    def test_move(self):
        r1 = Rectangle(2,2,4,4)
        r1.move(1,2)
        self.assertTrue(r1 != Rectangle(2,2,4,4))
        self.assertTrue(r1 == Rectangle(3,4,5,6))
        
    def test_intersection(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Rectangle(1,2,3,4).intersection(4)
        self.assertEqual(Rectangle(0,0,3,2).intersection(Rectangle(2,1,5,3)), Rectangle(2,1,3,2))
        self.assertNotEqual(Rectangle(0,0,3,2).intersection(Rectangle(2,1,5,3)), Rectangle(2,1,4,2))
        
    def test_cover(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Rectangle(1,2,3,4).intersection(4)
        self.assertEqual(Rectangle(0,0,3,2).cover(Rectangle(2,1,5,3)), Rectangle(0,0,5,3))
        self.assertNotEqual(Rectangle(0,0,3,2).cover(Rectangle(2,1,5,3)), Rectangle(2,1,5,3))
        
    def test_make4(self):
        L = [Rectangle(0,2,3,4), Rectangle(3,2,6,4), Rectangle(3,0,6,2), Rectangle(0,0,3,2)]
        self.assertEqual(Rectangle(0,0,6,4).make4(), L)
        
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test