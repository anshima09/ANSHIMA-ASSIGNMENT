def remove_empty_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("Content of the file before removing empty lines: ")
        for line in lines:
            print(line.strip())
    non_empty_lines = [line for line in lines if line.strip()]
    with open(filename, 'w') as file:
        file.writelines(non_empty_lines)
        print("Content of the file after removing empty lines: ")
        for line in non_empty_lines:
            print(line.strip())

remove_empty_lines("anshima.txt")