#kompilacja z python3

from points import Point
from math import *

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return True if (self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y) else False

    def __ne__(self, other):
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


