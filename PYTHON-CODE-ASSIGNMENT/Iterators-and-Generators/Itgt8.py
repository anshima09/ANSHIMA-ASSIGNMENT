def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


from itertools import islice
print("First 10 fibonacci numbers:")
print(list(islice(infinite_fibonacci(), 10)))
