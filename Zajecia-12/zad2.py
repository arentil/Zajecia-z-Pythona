#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

from random import randint

def rand(n, k):
    L = []
    for i in range(0,n):
        L.append(randint(0,k-1))
    return L

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
    
    
def binarne_rek(L, left, right, y):
    mid = int(left + ((right - left) / 2))
    if left >= right:
        return -1
    elif L[mid] == y:
        return mid
    elif L[mid] > y:
        return binarne_rek(L, left, mid - 1, y)
    elif L[mid] < y:
        return binarne_rek(L, mid + 1, right, y)
    

n = 30  # ilość elementów
k = 30  # zakres losowanych liczb

L = rand(30, 30)
heap_sort(L)    # sortujemy
print(L)
print("\nIndex: " + str(binarne_rek(L, 0, len(L), 15))) # wynik -1 oznacza, ze nie znaleziono