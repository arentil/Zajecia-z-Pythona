#kompilacja z python3

def factorial(n):
	a = 1;
	for i in range(int(n), 1, -1):
		a *= i
	return a

x = input("Podaj n-ty wyraz silni do wyswietlenia: ")
print(factorial(x))
