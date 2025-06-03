def even_numbers(limit):
    for num in range(0, limit + 1, 2):
        yield num

print("Even numbers up to 50:")
print(list(even_numbers(50)))
