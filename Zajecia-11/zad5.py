#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

'''
HEAPSORT

Algorytm sortowania w miejscu, niestabilny, o dobrej złożoności obliczeniowej O(n log n),
oraz pamięciowej O(n). Nieco wolniejszy od algorytmu quicksort.

'''


from zad1 import *


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def heapify(L, right,i):   
    l = 2 * i + 1  
    r = 2 * (i + 1)   
    max = i   
    if l < right and L[i] < L[l]:   
        max = l   
    if r < right and L[max] < L[r]:   
        max = r   
    if max != i:   
        swap(L, i, max)   
        heapify(L, right, max)   

def heap_sort(L):     
    right = len(L)   
    left = right // 2 - 1
    for i in range(left, -1, -1):   
        heapify(L, right, i)   
    for i in range(right - 1, 0, -1):   
        swap(L, i, 0)   
        heapify(L, i, 0)   

L = randomList(20)
heap_sort(L)
print(L)  
