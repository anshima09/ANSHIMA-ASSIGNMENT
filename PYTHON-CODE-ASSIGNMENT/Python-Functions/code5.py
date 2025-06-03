def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

str=input("Enter a string to count vowels: ")
print(f"The number of vowels in '{str}' is: ",count_vowels(str))