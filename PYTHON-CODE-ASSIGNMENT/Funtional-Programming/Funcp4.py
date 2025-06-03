def apply_func(func, lst):
    return [func(x) for x in lst]

result = apply_func(lambda x: x * 3, [1, 2, 3, 4])
print("Applied Function Result:", result)
