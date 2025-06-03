class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


print("Fibonacci sequence up to 10 terms:")
for num in FibonacciIterator(10):
    print(num, end=' ')
