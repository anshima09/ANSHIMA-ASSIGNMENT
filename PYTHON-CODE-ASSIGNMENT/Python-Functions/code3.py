def sum_and_average(lst):
    total = sum(lst)
    avg = total / len(lst) if lst else 0
    return total, avg

list=[54,21,34,89]
print("The sum and average of the list is ",sum_and_average(list)) 