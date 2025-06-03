def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])

pairs = [(1, 3), (2, 1), (4, 2)]
print("Unsorted:", pairs)
print("Sorted:", sort_by_second(pairs))