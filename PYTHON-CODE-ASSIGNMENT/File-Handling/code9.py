def count_characters(filename):
    freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


print("Character count in the file: ")
print(count_characters("anshima.txt"))
