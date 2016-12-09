#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
def bst_insert(top, data):   # zwraca nowy korzeń
    if top is None:
        return Node(data)
    if data < top.data:
        top.left = bst_insert(top.left, data)
    elif data > top.data:
        top.right = bst_insert(top.right, data)
    else:
        pass          # ignorujemy duplikaty
    return top            # bez zmian

def inorder(top):
    if top is None:
        return
    inorder(top.left)
    print(top.data)
    inorder(top.right)
    
    
def bst_max(top):
    if (top == None):
        raise ValueError("Empty tree!")
    node = top
    res = 0
    while (node):
        res = node.data
        node = node.right
    return res

def bst_min(top):
    if (top == None):
        raise ValueError("Empty tree!")
    node = top
    res = 0
    while (node):
        res = node.data
        node = node.left
    return res

root = bst_insert(None, 11)
root = bst_insert(root, 12)
root = bst_insert(root, 15)
root = bst_insert(root, 10)
root = bst_insert(root, 18)
root = bst_insert(root, 110)
root = bst_insert(root, 151)
root = bst_insert(root, 2)

print("Max: " + str(bst_max(root)))
print("Min: " + str(bst_min(root)))
