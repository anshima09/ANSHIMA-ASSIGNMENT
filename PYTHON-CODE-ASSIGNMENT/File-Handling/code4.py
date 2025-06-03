def append_input_to_file(filename):
    user_input = input("Enter text to append: ")
    with open(filename, 'r') as file:
        print("COntent of the file before appending: ")
        for line in file:
            print(line.strip())

    with open(filename, 'a') as file:
        file.write(user_input + '\n')

    with open(filename, 'r') as file:
        print("Content of the file after appending: ")
        for line in file:
            print(line.strip())

append_input_to_file("anshima.txt")