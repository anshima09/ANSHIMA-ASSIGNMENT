def is_list_palindrome(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True
list = [1, 2, 3, 2, 1]
print("List: ",list)
print("Is palindrome:", is_list_palindrome(list))