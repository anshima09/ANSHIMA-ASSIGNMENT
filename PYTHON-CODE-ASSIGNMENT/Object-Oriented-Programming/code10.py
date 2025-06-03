class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):  
    pass

obj = C()
obj.greet() 
print(C.__mro__) 
