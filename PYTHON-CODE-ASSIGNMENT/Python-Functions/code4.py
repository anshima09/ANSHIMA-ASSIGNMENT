def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

val=int(input("Enter the number of terms in the fibonacci sequence: "))
print("Fibonacci sequence: ",fibonacci(val))