class Queue:
    maxSize = 5
    queArray = [maxSize]
    front = 0
    rear = -1
    nItems = 0
    def __init__(self, size):
        self.maxSize = size
        self. queArray = [size]
    def insert(self, item):
        if(self.rear == self.maxSize-1): # deal with wraparound
            self.rear = -1
        self.rear+=1
        self.queArray[self.rear] = item; #increment rear and insert
        self.nItems+=1 # one more item
    def remove(self):
        self.front+=1
        temp = self.queArray[self.front]
        if(self.front == self.maxSize):
            self.front = 0
        self.nItems-=1
        return temp
    def peekFront(self):
        return self.queArray[self.front]
    def isEmpty(self):
        return self.nItems==0
    def isFull(self):
        return self.nItems==self.maxSize
    def size(self):
        return self.nItems
    def main():
        theQueue = Queue(5) # queue holds 5 items
        theQueue.insert(10) # insert 4 items
        theQueue.insert(20)
        theQueue.insert(30)
        theQueue.insert(40)
        theQueue.remove() # remove 3 items
        theQueue.remove() # (10, 20, 30)
        theQueue.remove()
        theQueue.insert(50) # insert 4 more items
        theQueue.insert(60) # (wraps around)
        theQueue.insert(70)
        theQueue.insert(80)
        while( not theQueue.isEmpty() ): #// remove and display all items
            n = theQueue.remove() #// (40, 50, 60, 70, 80)
            print(n) 
            print(" ")
