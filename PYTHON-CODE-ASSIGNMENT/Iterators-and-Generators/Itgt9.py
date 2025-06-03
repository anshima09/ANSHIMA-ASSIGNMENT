def read_lines(file):
    with open(file) as f:
        for line in f:
            yield line.strip()

def filter_lines(lines):
    return (line for line in lines if line)

def uppercase_lines(lines):
    return (line.upper() for line in lines)


print("Processing lines from 'anshima.txt':")
pipeline = uppercase_lines(filter_lines(read_lines('anshima.txt')))
for line in pipeline:
    print(line)
