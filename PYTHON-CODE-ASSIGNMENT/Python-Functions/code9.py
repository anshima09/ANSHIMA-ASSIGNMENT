def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print("The flatten list is: ",flatten_list([1, [2, [3, 4], 5], 6])) 