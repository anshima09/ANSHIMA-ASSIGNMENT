def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result

str=input("Enter a string to encrypt using caesar cipher: ")
shift=int(input("Enter the shift value: "))

print("Encrypted String: ",caesar_cipher(str,shift))  
