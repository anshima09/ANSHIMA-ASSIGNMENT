class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

s1 = Student("Bob", [85, 90, 78])
print("Average grade:", s1.average())
