class CharIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        ch = self.string[self.index]
        self.index += 1
        return ch

print("Characters in the string 'Anshima':")
for char in CharIterator("Anshima"):
    print(char)
