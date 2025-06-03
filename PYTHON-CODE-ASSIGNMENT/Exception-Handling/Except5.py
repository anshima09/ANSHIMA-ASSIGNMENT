def read_file(filename):
    try:
        file = open(filename, "r")
        print(file.read())
    except FileNotFoundError:
        print("File not found named",filename)
    finally:
        try:
            file.close()
        except:
            pass
read_file("sample.txt")
