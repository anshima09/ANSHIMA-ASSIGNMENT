def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            with open(file_name, 'r') as infile:
                print(f"Reading from {file_name}: ")
                outfile.write(infile.read() + '\n')
    with open(output_file, 'r') as outfile:
        print(f"Content of {output_file}: ")
        for line in outfile:
            print(line.strip())

merge_files(["anshima.txt", "anshima1.txt"], "merged.txt")