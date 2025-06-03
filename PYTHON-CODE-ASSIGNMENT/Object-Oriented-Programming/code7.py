class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        print("This is the child class (overridden)")

c = Child()
c.show()
