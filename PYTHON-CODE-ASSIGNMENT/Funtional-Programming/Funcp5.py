def power_fn(exp):
    return lambda x: x ** exp

square = power_fn(2)
cube = power_fn(3)
print("Square(5):", square(5))
print("Cube(2):", cube(2))
