class CircularListNode:
    def __init__(self, val):
        self.__init__(self,val)
    def __init__(self, val, next):
        self.val = val
        self.nextNode = next
    def main():
        current = CircularListNode(1)
        current = CircularListNode(2, current)
    print()