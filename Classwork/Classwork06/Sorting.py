class Sortable:
    def __init__(self,a):
        self.a  = a
    def insertion_sort( self ):
        for i in range( 1, len( self.a ) ):
            temp = self.a[i]
            print(temp)
            j = i - 1
            while( j >= 0 and temp < self.a[j] ):
                self.a[j+1] = self.a[j]
                j -= 1
            self.a[j+1] = temp
        return
def main():
    x = Sortable([1,5,4,6,2])
    x.insertion_sort()
    print(x.a)
main()