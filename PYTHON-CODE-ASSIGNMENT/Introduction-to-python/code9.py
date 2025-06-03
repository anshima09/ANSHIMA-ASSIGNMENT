number = int(input("Enter the number of Fibonacci terms: "))

a, b = 0, 1
count = 0

while count < number:
    print(a, end=" ")
    a, b = b, a + b
    count += 1