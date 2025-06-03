def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    print("Content of the file: ",text)
    return len(words)

print("Word count: ", count_words_in_file("anshima.txt"))