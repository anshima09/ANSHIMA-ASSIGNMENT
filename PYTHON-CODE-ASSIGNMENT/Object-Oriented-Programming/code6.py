class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)

mylist = MyList()
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)

print("My list first element: ",mylist[0])  
print("My list second element: ",mylist[1])  
print("My list third element: ",mylist[2])  
print("Length:", len(mylist))  
