class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name:
            self.__name = name

p = Person("John")
print("Getting name: ",p.get_name())
p.set_name("Doe")
print("Setting name: ",p.get_name())
