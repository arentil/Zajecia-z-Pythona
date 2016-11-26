#kompilacja z python3

from math import *
import unittest

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie"""
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        return True if (self.x == other.x and self.y == other.y) else False

    def __ne__(self, other):
        return not self == other
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)