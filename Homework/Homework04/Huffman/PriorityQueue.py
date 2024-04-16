class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[0]

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0][0]

    def __str__(self):
        return ", ".join(f"[{item}:{priority}" for item, priority in self.queue)

    def __len__(self):
        return len(self.queue)