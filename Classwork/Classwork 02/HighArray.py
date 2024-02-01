###
# filename: HighArray.py
# author: Makari Green, Ayre Mindell, Stephen Ude
# date:     2024-01-28
###

# global to the entire file
a = []         # empty list

# the class
class HighArray():

   # fields
    a = []

   # initializer
    def __init__(self, maxSize):
        a = []         # initialize the list to be empty [still]

   # find if a value is in the list
    def find(self, value):
        for x in self.a:
            if(x == value):
                return True
        return False

   # insert a value at the end of the list
    def insert(self, value):
        self.a.append(value)
        return

   # delete a specific value
    def delete(self, value):
        self.a.remove(value)
        return value

   # display
    def display(self):
        print(self.a)
        return

   # get max goes here
    def getMax(self):
        x=self.a[0]
        for y in self.a:
            if( y > x):
                x = y
        return x

   # noDupes goes here
    def noDupes(self):
        for x in a:
            if x not in a:
                self.a.append(x)
  #      m = []
   #     for x in self.a:
    #        if(x not in m):
     #           m.append(x)
      #  self.a.clear()
       # for x in m:
        #    self.a.append(x)
        #return self.a



# a little test to make sure the interpreter won't barf
h1 = HighArray( 10 )
h1.display()