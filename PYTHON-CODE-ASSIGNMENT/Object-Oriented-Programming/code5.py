class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

    def show_count(self):
        print("Current count:", Counter.count)

a = Counter()
b = Counter()
c = Counter()
c.show_count()  
