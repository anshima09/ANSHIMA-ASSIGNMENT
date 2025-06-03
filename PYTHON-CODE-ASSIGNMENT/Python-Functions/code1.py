def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

val=int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {val} is: ",factorial(val))