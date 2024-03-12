class Queue:
    def __init__(self, size):
        self.maxSize = size
        self.queArray = [None] * size
        self.front = 0
        self.rear = -1
        self.nItems = 0

    def insert(self, item):
        if self.rear == self.maxSize - 1:  # deal with wraparound
            self.rear = -1
        self.rear += 1
        self.queArray[self.rear] = item
        self.nItems += 1

    def remove(self):
        self.front += 1
        temp = self.queArray[self.front]
        if self.front == self.maxSize:
            self.front = 0
        self.nItems -= 1
        return temp

    def peekFront(self):
        return self.queArray[self.front]

    def isEmpty(self):
        return self.nItems == 0

    def isFull(self):
        return self.nItems == self.maxSize

    def size(self):
        return self.nItems


def main():
    theQueue = Queue(5)
    theQueue.insert(10)
    theQueue.insert(20)
    theQueue.insert(30)
    theQueue.insert(40)
    theQueue.remove()
    theQueue.remove()
    theQueue.remove()
    theQueue.insert(50)
    theQueue.insert(60)
    theQueue.insert(70)
    theQueue.insert(80)

    while not theQueue.isEmpty():
        n = theQueue.remove()
        print(n)
        print("")


if __name__ == "__main__":
    main()
