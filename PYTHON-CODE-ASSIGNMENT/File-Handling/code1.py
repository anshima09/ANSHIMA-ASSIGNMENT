def print_file_with_line_numbers(filename):
    with open(filename, 'r') as file:
        for idx, line in enumerate(file, start=1):
            print(f"{idx}: {line.strip()}")

print_file_with_line_numbers("anshima.txt")