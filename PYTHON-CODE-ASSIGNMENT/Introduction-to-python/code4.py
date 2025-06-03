number = int(input("Enter an integer: "))
rev_num = 0
original = abs(number)

while original > 0:
    d = original % 10
    rev_num = rev_num * 10 + d
    original //= 10

if number < 0:
    rev_num = -rev_num

print(f"Reversed number: {rev_num}")