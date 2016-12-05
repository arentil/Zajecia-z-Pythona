#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if ((a + c <= b) or (a + b <= b) or (b + c) <= a):  #sprawdzam "poprawność" długości boków trójkąta
        raise ValueError("Invalid arguments!")
    
    #korzystamy ze wzoru herona
    p = 0.5 * (a + b + c)
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    #równoważnie:
    # s = sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
    return s

print("Podaj długości boków trójkąta do obliczenia jego pola:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
try:
    result = heron(a,b,c)
except ValueError:
    print("Nie da się zbudować trójkąta o zadanych bokach!")
else:
    print("Pole trójkąta: " + str(heron(a,b,c)))