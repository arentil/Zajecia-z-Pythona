#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

"""
    P(0, 0) = 0.5,
    P(i, 0) = 0.0 dla i > 0,
    P(0, j) = 1.0 dla j > 0,
    P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
"""

import time

def Pr(i, j):               #rekurencyjnie
    if (i < 0 or j < 0):
        raise ValueError("Invalid arguments!")
    if (i == 0 and j == 0):
        return 0.5
    if (i > 0 and j == 0):
        return 0.0
    if (i == 0 and j > 0):
        return 1.0
    return (0.5 * Pr(i - 1, j)) + Pr(i, j - 1)


S = {(0,0): 0.5, (0,1): 1.0, (1,0): 0.0}    #słownik
def Pd(i, j):               #dynamicznie
    global S
    if (i < 0 or j < 0):
        raise ValueError("Invalid arguments!")
    if (i == 0 and j == 0):
        return 0.5
    if (i > 0 and j == 0):
        return 0.0
    if (i == 0 and j > 0):
        return 1.0
    d = S.get((i, j))
    if (d != None):
        return d
    else:
        d = 0.5 * (Pd(i-1, j) + Pd(i, j-1))
        S[(i,j)] = d
        return d

def compare(i, j):
    prtime = time.time()
    rres = Pr(i,j)
    print("Funkcja P(" + str(i) + ", " + str(j) + ") rekurencja w czasie: " + str(time.time() - prtime))
    pdtime = time.time()
    dres = Pd(i, j)
    print("Funkcja P(" + str(i) + ", " + str(j) + ") dynamicznie w czasie: " + str(time.time() - pdtime))
    
compare(10, 15)