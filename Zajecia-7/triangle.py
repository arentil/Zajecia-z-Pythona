#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from points import Point
from math import *

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        if ((x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3)):
            raise ValueError("Invalid arguments!")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[(%s, %s), (%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle(%s, %s, %s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):
        if (not isinstance(other, Triangle)):
            raise ValueError("Invalid arguments!")
        return True if (self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3) else False
        
    def __ne__(self, other):        # obsługa tr1 != tr2
        if (not isinstance(other, Triangle)):
            raise ValueError("Invalid arguments!")
        return not self == other

    def center(self):         # zwraca środek trójkąta
        return (Point(((self.pt1.x + self.pt2.x + self.pt3.x) / 3), ((self.pt1.y + self.pt2.y + self.pt3.y) / 3)))

    def area(self):       # pole powierzchni
        return (abs((self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y)) / 2))

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x; self.pt1.y += y
        self.pt2.x += x; self.pt2.y += y
        self.pt3.x += x; self.pt3.y += y

    def make4(self):          # zwraca listę czterech mniejszych
        pt4 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        pt5 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        pt6 = Point((self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2)
        tri1 = Triangle(self.pt1.x, self.pt1.y, pt4.x, pt4.y, pt6.x, pt6.y)
        tri2 = Triangle(pt4.x, pt4.y, self.pt2.x, self.pt2.y, pt5.x, pt5.y)
        tri3 = Triangle(pt6.x, pt6.y, pt5.x, pt5.y, self.pt3.x, self.pt3.y)
        tri4 = Triangle(pt4.x, pt4.y, pt5.x, pt5.y, pt6.x, pt6.y)
        return [tri1, tri2, tri3, tri4]