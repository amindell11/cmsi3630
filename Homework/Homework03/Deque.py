class Deque:

   def __init__(self,size): 
      self.size = size #Initialize the deque
      self.queue = [None]*size #creates a list to store deque elements
      self.front = 0 # initializes front pointers
      self.rear = -1 #initializes rear pointers
      self.items = 0 #initializes number of items in deque
   
   def insertLeft(self, items):
      if self.isFull(): #checks if deque is full
         print("Deque is empty")
      self.rear = (self.rear + 1)%self.size #updates rear pointer and insert item
      self.queue.insert(self.front, items)
      self.items += 1 #increment number of items
   
   def insertRight(self, items):
      if self.isFull():
         print("Deque is full")
      self.rear = (self.rear - 1)%self.size
      self.queue.insert(self.rear, items)
      self.items += 1
   def removeLeft(self):
      if self.isEmpty():
         print("Deque is empty")
      items = self.queue[self.rear]
      self.rear = (self.rear - 1) % self.size
      self.items -= 1
      return items
   def removeRight(self):
      if self.isEmpty():
         print("Deque is empty")
      items = self.queue[self.front]
      self.front = (self.front + 1) % self.size
      self.items -= 1
      return items
   def isEmpty(self):
      return self.items == 0
   def isFull(self):
      return self.items == self.size
   def printDeque(self):
      print("Deque:", end=" [")
      for i in range(self.size):
         if i > 0:
            print(", ", end="")
         print(self.queue[i], end="")
      print(']')
   
   

def main():
   deque_start = Deque(5)
   deque_start.insertLeft(10)
   deque_start.insertRight(20)
   deque_start.insertLeft(30)
   deque_start.insertRight(40)
   deque_start.removeLeft()
   deque_start.removeRight()
   deque_start.removeLeft()
   deque_start.insertLeft(50)
   deque_start.insertRight(60)
   deque_start.insertLeft(70)
   deque_start.insertRight(80)

   deque_start.printDeque()
   print("Is deque empty?", deque_start.isEmpty())
   print("Is deque full?", deque_start.isFull())

if __name__ == "__main__":
    main()