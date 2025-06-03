def replace_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in s:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result

str=input("Enter a string: ")
print("Replaced vowels with *, string becomes: ",replace_vowels(str))