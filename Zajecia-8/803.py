#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

"""
    Do wykonania programu posłużyłem się funkcją pomocniczą o nazwie "isPointInCircle"
    zwracającej true jeżeli punkt znajduje się w okręgu lub false jeżeli się nie znajduje
    (ale znajduje się w kwadracie z opisanym w środku okręgiem)
    Kwadrat o boku 1, więc z punktem środkowym koła jest punkt 0.5,0.5, promien wynosi 0.5
"""

from math import sqrt
from random import random

def isPointInCircle(x, y):
    res = sqrt(((x - 0.5) ** 2) + ((y - 0.5) ** 2))
    if (res < 0.5):
        return True
    else:
        return False
    

def calc_pi(n = 100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inside = 0
    for i in range(n):
        if (isPointInCircle(random(), random())):
            inside += 1
    pi = 4 * (inside / n)
    return pi
    
print("     Iteracji:\tPI:")
print("\t10: \t" + str(calc_pi(10)))
print("\t100: \t" + str(calc_pi(100)))
print("\t1000: \t" + str(calc_pi(1000)))
print("\t10000: \t" + str(calc_pi(10000)))
print("\t100000:\t" + str(calc_pi(100000)))