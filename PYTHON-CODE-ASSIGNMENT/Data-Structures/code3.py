def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

items = [1, 2, 2, 3, 4, 4, 5]
print("With duplicates:", items)
print("Without duplicates:", remove_duplicates(items))