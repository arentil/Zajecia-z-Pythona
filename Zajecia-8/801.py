#!/usr/bin/python
# -*- coding: utf-8 -*-
#kompilacja z python3

"""
ALGORYTM - LISTA KROKÓW:

1. Podaj a, b, c
2. Jeżeli a = 0 i b = 0
    2a. Jeżeli c = 0, to wypisz: "Równanie nieokreślone"
    2b. W przeciwnym wypadku wypisz: "Równanie sprzeczne. c = 0"
3. Jeżeli a = 0 to wypisz: "Rozwiązanie - prosta: y = (-c / b)"
4. Jeżeli b = 0 to wypisz: "Rozwiązanie - prosta: x = (-c / a)"
5. Jeżeli nie zaszło 2 ani 3 ani 4 to wypisz: "Rozwiązanie: y = (-a / b)x + (-c/b)"
"""

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if (a == 0 and b == 0):
        if (c == 0):
            print("Równanie nieokreślone. a = 0, b = 0, c = 0")
            return
        else:
            print("Równanie spczeczne. " + str(c) + " = 0")
            return
    if (a == 0):
        print("Rozwiązanie - prosta: y = " + str(-c / b))
        return
    if (b == 0):
        print("Rozwiązanie - prosta x = " + str(-c / a))
        return
    result = "y = " + str(-a / b) + "x " + ("+ " if (-c / b) > 0 else "") + str(-c / b)
    print("Rozwiązanie: " + result)
    return
    
print("Podaj:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
solve1(a,b,c)