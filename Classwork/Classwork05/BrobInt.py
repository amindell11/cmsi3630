###
# filename: BrobIntEmpty.py
# purpose:  a python 'Big Integer' class
# author:   Dr. Johnson
# date:     2023-02-08
#
# DOWNLOAD THIS FILE TO USE AS A STARTING EDIT
# RENAME IT TO "BrobInt.py" REMOVING THE 'EMPTY'
# FILL IN THE CODE FOR THE "add()" METHOD
# THE TEST CODE IS ALREADY GIVEN TO YOU
###


class BrobInt:

   backwards  = []
   digits   = []
   string_rep = ''
   value = 0

   def __init__( self, value ):
      self.string_rep = value
      self.digits   = [*self.string_rep]      # this is the 'unpacking' operator
      self.backwards  = self.reverse_me()
      self.value  = int("".join(self.digits))
   
   @staticmethod
   def reverse( a ):
      b = []
      j = len( a ) - 1
      for i in a:
         b.append( a[j] )
         j -= 1
      return b
   def reverse_me( self ):
      return BrobInt.reverse(self.digits)
   ## TODO: implement the addition function by filling in the
   ##   code under the comments below
   def add( self, other_brob_int ):
      sum = []
      shorter = []
      longer = []
      if(self.value<other_brob_int.value):
         shorter = self.backwards
         longer = other_brob_int.backwards
      else :
         shorter = other_brob_int.backwards
         longer = self.backwards
      ## find the lengths of the two number
      short_len = len(shorter)
      longer_len = len(longer)
      print(f"values: {short_len} long: {longer_len}")
      carry = 0
      for i in range(short_len):
         digit = int(shorter[i])+int(longer[i])+carry
         print(f"adding: {shorter[i]} and: {longer[i]} with carry {carry} result = {digit}")
         if(digit>9):
            digit_ceil = digit % 10
            carry = int((digit-digit_ceil)/10)
            digit = int(digit_ceil)
         else:
            carry = 0
         sum.append(str(digit))
      if(carry!=0):
         sum.append(str(int(carry)))
      sum.append(str(int(int(longer[short_len])+carry)))
      sum=sum+longer[short_len+1:longer_len]
      print(sum)
      ## add up the two numbers,
      ##   stopping after the shorter one has been added
      ##   to the shortest part of the longer one

      ## Now if they are NOT the same length
      ##   add the carry [if needed] to the next digit of
      ##   the longer number, then continue adding in the
      ##   rest of the longer number

      ## If there is still a carry, handle it

      ## turn it back into a string and return the result

      print( "\n   OOPS!  Sorry, 'add()' not implemented yet." )
      sum = BrobInt.reverse( sum )
      return_value = "".join( sum )
      return return_value


b1 = BrobInt( '123456789' )
b2 = BrobInt( '13579' )
b3 = BrobInt( '2468')
b4 = BrobInt( '102030405060708090')
b5 = BrobInt( '123456784567890234567456782345623453456782345611234567')
b6 = BrobInt( '9999' )
print( "   sum of b1 and b2:\n   expecting: 123470368\n         got:", b1.add( b2 ) )
print( "   sum of b2 and b1:\n   expecting: 123470368\n         got:", b2.add( b1 ) )
print( "   sum of b3 and b4:\n   expecting: 102030405060710558\n         got:", b3.add( b4 ) )
print( "   sum of b4 and b5:\n   expecting: 123456784567890234567456782345623453558812750671942657\n         got:", b4.add( b5 ) )
print( "   sum of b3 and b6:\n   expecting: 12467\n         got:", b3.add( b6 ) )
