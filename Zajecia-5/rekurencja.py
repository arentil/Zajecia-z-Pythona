def factorial(n):
	a = 1;
	for i in range(int(n), 1, -1):
		a *= i
	return a
    
def fibonacci(n):
    a = 0
    b = 1
    if (n == 0): 
            return 0
    for i in range(1, n):
            b += a
            a = b-a
                    
    return b