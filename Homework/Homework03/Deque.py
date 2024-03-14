class Deque:

   def __init__(self,size): 
      self.size = size #Initialize the deque
      self.queue = [ ]*size #creates a list to store deque elements
      self.front = 0 # initializes front pointers
      self.rear = -1 #initializes rear pointers
      self.items = 0 #initializes number of items in deque
   
   def insertLeft(self, item):
      if self.isFull(): #checks if deque is full
         print("Deque is Full")
      self.rear = (self.rear + 1)%self.size #updates rear pointer and insert item
      self.queue[self.rear] = item
      self.items += 1 #increment number of items
   
   def insertRight(self, item):
      if self.isFull():
         print("Deque is Full")
      self.rear = (self.rear - 1)%self.size
      self.queue[self.rear] = item
      self.items += 1
   def removeLeft(self):
      if self.isEmpty():
         print("Deque is Full")
      item = self.queue[self.rear]
      self.rear = (self.rear - 1) % self.size
      self.items -= 1
      return item
   def removeRight(self):
      if self.isEmpty():
         print("Deque is Full")
      item = self.queue[self.front]
      self.front = (self.front + 1) % self.size
      self.items -= 1
      return item
   def isEmpty(self):
      return self.item == 0
   def isFull(self):
      return self.ietms == self.size
   


