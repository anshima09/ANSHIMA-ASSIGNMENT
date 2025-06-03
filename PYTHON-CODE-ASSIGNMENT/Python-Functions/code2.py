def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


input_str = input("Enter a string to check for palindrome: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")