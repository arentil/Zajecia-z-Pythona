#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3


from random import shuffle, gauss, randint
from math import floor, sqrt

def randomList(n):
    L = list(range(n))
    shuffle(L)
    return L

def almostSortedList(n):
    L = list(range(n))
    i = 0
    while (i < n-1):
        L[i], L[i+1] = L[i+1], L[i]
        i = i+2
    return L

def almostSortedReversedList(n):
    L = list(reversed(range(n)))
    i = 0
    while (i < n-1):
        L[i], L[i+1] = L[i+1], L[i]
        i = i+2
    return L

def gaussRandomList(n):
    L = [round(gauss(n/2, n/6)) for _ in range(n)]
    return L

def repeatedRandomList(n):
    L = [randint(0,floor(sqrt(n))) for _ in range(n)]
    return L