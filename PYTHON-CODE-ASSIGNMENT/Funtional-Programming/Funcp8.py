numbers = range(1, 11)
pipeline = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print("Pipeline Result (Even × 2):", pipeline)
