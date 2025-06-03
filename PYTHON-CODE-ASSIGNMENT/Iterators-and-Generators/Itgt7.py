words = ['madam', 'hello', 'racecar', 'world']
palindromes = (word for word in words if word == word[::-1])
print("Palindromes in the list:")
print(list(palindromes))
