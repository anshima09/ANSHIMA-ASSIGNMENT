from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print("Factorial of 7:", factorial(7))
