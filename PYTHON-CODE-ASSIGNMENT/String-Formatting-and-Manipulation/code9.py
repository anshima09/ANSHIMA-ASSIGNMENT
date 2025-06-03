def longest_palindrome(s):
    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(longest):
                longest = substr
    return longest

str = input("Enter a string to find the longest palindrome: ")
print("Longest Palindrome: ",longest_palindrome(str))  
