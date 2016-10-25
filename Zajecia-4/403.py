def factorial(n):
	x = 1;
	for i in range(int(n), 1, -1):
		x *= i
	return x

print factorial(raw_input())
