#kompilacja z python3

import unittest
from rectangle import *

class TestRectangle(unittest.TestCase):

    def setUp(self): pass
        
    def test_str_rect(self):
        self.assertEqual(str(Rectangle(1,2,3,4)), "[(1, 2), (3, 4)]")
        
    def test_eq_rect(self):
        self.assertTrue(Rectangle(1,2,3,4) == Rectangle(1,2,3,4))
        self.assertFalse(Rectangle(4,3,2,1) == Rectangle(1,2,3,4))
        
    def test_ne_rect(self):
        self.assertFalse(Rectangle(1,2,3,4) != Rectangle(1,2,3,4))
        self.assertTrue(Rectangle(4,3,2,1) != Rectangle(1,2,3,4))
        
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
        
        
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test