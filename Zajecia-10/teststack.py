#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

import unittest
from stack import *

class TestStack(unittest.TestCase):
    
    def setUp(self): pass
    
    
    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(2)
        self.assertFalse(s.is_empty())
        
        
    def test_is_full(self):
        s = Stack(2)
        self.assertFalse(s.is_full())
        s.push(1)
        self.assertFalse(s.is_full())
        s.push(2)
        self.assertTrue(s.is_full())
        
        
    def test_push(self):
        s = Stack(5)
        self.assertEqual(s.n, 0)
        s.push(1)
        self.assertEqual(s.n, 1)
        s.push(2)
        self.assertEqual(s.n, 2)
        s.push(3)
        s.push(4)
        s.push(5)
        try:
            s.push(6)
        except Exception as e:
            self.assertEqual(str(e), "Stack full!")
        
        
    def test_pop(self):
        s = Stack(3)
        s.push(1)
        self.assertEqual(s.pop(), 1)
        try:
            s.pop()
        except Exception as e:
            self.assertEqual(str(e), "Stack empty!")
            

    def tearDown(self): pass



if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie test