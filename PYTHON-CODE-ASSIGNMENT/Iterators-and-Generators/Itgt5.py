def line_reader(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()
for line in line_reader('anshima.txt'):
    print(line)
