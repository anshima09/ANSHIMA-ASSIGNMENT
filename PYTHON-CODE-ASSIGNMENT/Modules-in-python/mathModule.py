import math

num = int(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
power = int(input("Enter the power to raise to: "))
print(f"{num}^{power} =", math.pow(num, power))
