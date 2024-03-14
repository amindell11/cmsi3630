class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
   

class CircularList:
   def __init__(self):
      self.head = None
   def insert(self, data):
      newNode = Node(data)
      
      if not self.head:
         newNode.next = newNode
         self.head = newNode
      else:
         newNode.next = self.head.next
         self.head.next = newNode

   def remove(self):
      
      if not self.head:
         raise IndexError("Circular List is empty")
      removeNode = self.head.next
      if self.head.next == self.head:
         self.head = None
      else:
         self.head.next = removeNode.next
      return removeNode.data

class Stack:
   def __init__(self):
      self.circular_list = CircularList()
   def push(self, data):
      self.circular_list.insert(data)   
   def pop(self):
      return self.circular_list.remove()
   def isEmpty(self):
      return self.circular_list.head


stack_start = Stack()
stack_start.push(10)
stack_start.push(20)
stack_start.push(30)


print(stack_start.pop())
print(stack_start.pop())
print(stack_start.pop())






   



