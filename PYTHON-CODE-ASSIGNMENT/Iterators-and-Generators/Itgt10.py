from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'r')
    try:
        yield f
    finally:
        f.close()

print("Reading lines from 'anshima.txt':")

with open_file('anshima.txt') as file:
    for line in file:
        print(line.strip())
