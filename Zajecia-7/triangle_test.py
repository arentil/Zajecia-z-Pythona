#kompilacja z python3

import unittest
from triangle import *

class TestTriangle(unittest.TestCase):
    
    def setUp(self): pass

    def test_init_tri(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Triangle(1,2,1,3,1,5)
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
           Triangle(1,2,4,2,6,2)
           
    def test_str_tri(self):
        self.assertEqual(str(Triangle(0,0,1.5,1.5,0,3)), "[(0, 0), (1.5, 1.5), (0, 3)]")
        
    def test_eq_tri(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
            Triangle(0,0,2,2,0,3) == 4
        self.assertTrue(Triangle(0,0,2,2,0,3) == Triangle(0,0,2,2,0,3))
        self.assertFalse(Triangle(0,0,2,2,0,3) == Triangle(0,0,1.5,1.5,0,3))
    
    def test_ne_tri(self):
        with self.assertRaisesRegex(ValueError, "Invalid arguments!"):
            Triangle(0,0,2,2,0,3) == 4
        self.assertFalse(Triangle(0,0,2,2,0,3) != Triangle(0,0,2,2,0,3))
        self.assertTrue(Triangle(0,0,2,2,0,3) != Triangle(0,0,1.5,1.5,0,3))
           
    def test_area_tri(self):
        self.assertEqual(Triangle(0,0,1,2,2,0).area(), 2)
        self.assertEqual(Triangle(0,0,1.5,1.5,0,3).area(), 2.25)
        
    def test_move_tri(self):
        tri = Triangle(0,0,1,2,2,0)
        tri.move(2,2)
        self.assertEqual(tri, Triangle(2,2,3,4,4,2))
           
           
    def test_make4(self):
        L = [Triangle(0, 0, 0.5, 1, 1, 0), Triangle(0.5, 1, 1, 2, 1.5, 1), Triangle(1, 0, 1.5, 1, 2, 0), Triangle(0.5, 1, 1.5, 1, 1, 0)]
        self.assertEqual(Triangle(0,0,1,2,2,0).make4(), L)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test