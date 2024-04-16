class BinaryHeap:

    list = []
    size  = 0

    def __init__( self ):
        self.list = []
        return

    # First some low-hanging fruit; let's do the traversal helpers that do the
    #  indexing operations that we'll need to use for finding stuff in the heap
    # NOTE: Python sees the quotient of a division as a 'float', so you must
    #  convert it to an 'int' to be able to use it to index a list
    def get_parent( self, index ):
        return self.list[(int)((index - 1) / 2)]

    def get_child( self, index, child ):
        result = (index * 2) + 1
        if( child.upper() == 'R'):
            result += 1
        return self.list[result]

    # this just prints the array values; it's left to the observer to figure out
    #  which HeapNode is which, in terms of parent and child
    def print_heap( self ):
         for val in self.list:
            print( "[", val, "]", end = "" )
         print()
         
    def insert( self, value ):
        self.list.append(value)
        self.bubble_up( self.size )                # WOW that was easy!
        self.size += 1
        
    def remove(self):
        return_val = self.list.pop()
        temp = self.list[0]
        self.list[0] = self.list[self.size-1]
        self.list[self.size-1] = temp
        self.trickle_down(self.size-1)
        return return_val
    
    def trickle_down( self, index):
        child_index = (index * 2) + 1
        if(child_index>self.size):
                return
        elif(self.list[child_index] >self.list[index]):
            parent = self.get_parent( index )
            parent_index = (int)((index -1) / 2)
            if( self.list[parent_index] < self.list[index] ):
                temp = self.list[index]
                self.list[index] = self.list[parent_index]
                self.list[parent_index] = temp
                self.bubble_up( parent_index )
    # Here is the bubble method that does the swappy thang....
    #  Whaddya mean?!  OF COURSE it is recursive!  Fuggeddaboutit...
    def bubble_up( self, index ):
        if( index == 0 ):     # base case:
            return             #  we are already at the root, so we are done
        parent = self.get_parent( index )
        parent_index = (int)((index -1) / 2)
        if( self.list[parent_index] < self.list[index] ):
            temp = self.list[index]
            self.list[index] = self.list[parent_index]
            self.list[parent_index] = temp
            self.bubble_up( parent_index )
def main():
    heap = BinaryHeap()
    heap.insert(17)
    heap.insert(11)
    heap.insert(13)
    heap.insert(19)
    heap.insert(25)
    heap.insert(23)
    heap.insert(29)
    heap.print_heap()
main()