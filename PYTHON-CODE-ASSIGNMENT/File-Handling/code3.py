def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        for line in src:
            dest.write(line)

copy_file("anshima.txt", "example.txt")
print("File copied succesffuly from", "anshima.txt", "to", "example.txt")
print("Content of the copied file: ")

with open("example.txt", 'r') as f:
    for line in f:
        print(line.strip())