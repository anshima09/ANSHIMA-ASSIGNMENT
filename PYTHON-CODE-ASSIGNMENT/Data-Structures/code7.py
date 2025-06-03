from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Queue is empty"


q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(45)
q.enqueue(34)
print("Dequeue:", q.dequeue())