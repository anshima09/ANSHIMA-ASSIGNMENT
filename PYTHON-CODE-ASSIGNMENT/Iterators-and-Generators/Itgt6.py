def cartesian_product(a, b):
    for x in a:
        for y in b:
            yield (x, y)

print("Cartesian product of [1,2] and ['a','b']:")
print(list(cartesian_product([1, 2], ['a', 'b'])))
