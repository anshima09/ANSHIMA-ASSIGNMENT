number = int(input("Enter an integer: "))
reversed_number = 0
original = abs(number)

while original > 0:
    digit = original % 10
    reversed_number = reversed_number * 10 + digit
    original //= 10

if number < 0:
    reversed_number = -reversed_number

print(f"Reversed number is : {reversed_number}")