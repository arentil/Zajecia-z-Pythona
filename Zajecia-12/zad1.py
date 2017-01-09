#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from random import randint

def rand(n, k):
    L = []
    for i in range(0,n):
        L.append(randint(0,k-1))
    return L


def linear_search(L, left, right, y):
    """Wyszukiwanie liniowe w ciągu."""
    retL = []
    i = left
    while i < right:
        if y == L[i]:
            retL.append(i)
        i = i + 1
    return retL


n = 100
k = 10
y = 5

L = rand(n, k)
print(L)
print()
print(linear_search(L, 0, len(L), y))