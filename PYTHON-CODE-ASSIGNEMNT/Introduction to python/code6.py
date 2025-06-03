expr = input("Enter an expression (e.g., 4 + 5): ")
tokens = expr.split()

if len(tokens) == 3:
    a, op, b = tokens
    a = float(a)
    b = float(b)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operator"
else:
    result = "Invalid input format"

print("Result:", result)