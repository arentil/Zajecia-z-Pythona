def factorial(n):
	a = 1;
	for i in range(int(n), 1, -1):
		a *= i
	return a

x = input("Podaj n-ty wyraz silni do obliczenia:")
print(factorial(x))
