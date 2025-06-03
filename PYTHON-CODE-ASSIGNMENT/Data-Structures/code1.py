def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

nums = [1, 2, 3, 4, 5]
print("Original:", nums)
print("Reversed:", reverse_list(nums))