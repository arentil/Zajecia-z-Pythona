#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from points import Point
from math import *

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if (x1 > x2 or y1 > y2):
            raise ValueError("Invalid arguments!")
        
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        if (not isinstance(other, Rectangle)):
            raise ValueError("Invalid arguments!")
        return True if (self.pt1 == other.pt1 and self.pt2 == other.pt2) else False

    def __ne__(self, other):
        if (not isinstance(other, Rectangle)):
            raise ValueError("Invalid arguments!")
        return not self == other

    def center(self):
        return Point(((self.pt1.x + self.pt2.x) / 2), ((self.pt1.y + self.pt2.y) / 2))

    def area(self):    
        return (abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y))

    def move(self, x, y):   
        self.pt1.x += x;
        self.pt2.x += x;
        self.pt1.y += y;
        self.pt2.y += y;

    def intersection(self, other):  # część wspólna prostokątów
        if (not isinstance(other, Rectangle)):
            raise ValueError("Invalid arguments!")
        result = Rectangle()
        result.pt1.x = max(self.pt1.x, other.pt1.x)
        result.pt2.x = min(self.pt2.x, other.pt2.x)
        result.pt1.y = max(self.pt1.y, other.pt1.y)
        result.pt2.y = min(self.pt2.y, other.pt2.y)
        return result

    def cover(self, other):   # prostąkąt nakrywający oba
        if (not isinstance(other, Rectangle)):
            raise ValueError("Invalid arguments!")
        result = Rectangle()
        result.pt1.x = min(self.pt1.x, other.pt1.x)
        result.pt2.x = max(self.pt2.x, other.pt2.x)
        result.pt1.y = min(self.pt1.y, other.pt1.y)
        result.pt2.y = max(self.pt2.y, other.pt2.y)
        return result

    def make4(self):     # zwraca listę czterech mniejszych
        mid = self.center() #punkt srodkowy
        rec1 = Rectangle(self.pt1.x, mid.y, mid.x, self.pt2.y)  #lewy gorny kwadrat
        rec2 = Rectangle(mid.x, mid.y, self.pt2.x, self.pt2.y)  #prawy gorny    
        rec3 = Rectangle(mid.x, self.pt1.y, self.pt2.x, mid.y)  #prawy dolny
        rec4 = Rectangle(self.pt1.x, self.pt1.y, mid.x, mid.y)  #lewy dolny
        return [rec1, rec2, rec3, rec4]