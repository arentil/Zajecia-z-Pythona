#kompilacja z python3
#!/usr/bin/python

import rekurencja

print(rekurencja.factorial(1))
print(rekurencja.fibonacci(2))

import rekurencja as rek

print(rek.factorial(3))
print(rek.fibonacci(4))

from rekurencja import *

print(factorial(5))
print(fibonacci(6))

from rekurencja import factorial

print(factorial(7))

from rekurencja import fibonacci as fib

print(fib(5))


