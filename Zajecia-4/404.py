def fibonacci(n):
	a = 0
	b = 1
	if (n == 0): 
		return 0
	for i in range(1, n):
		b += a
		a = b-a
			
	return b

x = raw_input("Podaj n-ty wyraz ciagu fibonacciego:")
print fibonacci(int(x))
