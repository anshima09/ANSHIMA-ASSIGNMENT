def replace_words_in_file(filename, replacements):
    with open(filename, 'r') as file:
        content=file.read()
        print("Content of the file before replacement: ",content)
        
    for old_word, new_word in replacements.items():
        content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)
    with open(filename, 'r') as file:
        print("Content of the file after replacement: ")
        for line in file:
            print(line.strip())

replacements = {
    "Hello": "Hi",
    "anshima": "garima"
}
replace_words_in_file("anshima.txt", replacements)
