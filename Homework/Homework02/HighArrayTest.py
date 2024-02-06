###
# filename: HighArrayTest.py
# author:  Makari Green, Stephen Ude, Arye Mindell
# date:     2024-01-28
###

from HighArray import HighArray

print( "\n   Welcome to the HighArray Miltary Program [Python Version]" )
print( "   Where we train the best and nothing but the best" )
print( "   Initializing the list" )
arr = HighArray( 100 )
print( arr )

print( "   Adding ten items" )
arr.insert( 77 )                 # insert 10 items
arr.insert( 99 )
arr.insert( 44 )
arr.insert( 55 )
arr.insert( 22 )
arr.insert( 88 )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )

print( "\n   Current list contents:" )
arr.display()

print( "\n   Searching for 37:" )
found = arr.find( 37 )
if( found ):
   print( "Target Acquired!" )
else:
   print( "Charlie went AWOL..." )

print( "\n   Searching for 11:" )
found = arr.find( 11 )
if( found ):
   print( "Target Acquired!" )
else:
   print( "Charlie went AWOL..." )

print( "\n   Adding and removing to test getMax function..." )
print( "   [first removing three items: 0, 55, and 99]" )
arr.delete( 00 )          # delete 3 items
arr.delete( 55 )
arr.delete( 99 )
arr.display()             # display items again
print( "   Max value in array/list is now: ", arr.getMax() )
print( "   Adding 99 back in" )
arr.insert( 99 )
print( "   Max value in array/list is now: ", arr.getMax() )
arr.display()
print( "   Eradicating max value...", arr.delete(arr.getMax()) )
print( "   Eradicating max value...", arr.delete(arr.getMax()) )
print( "   Eradicating max value...", arr.delete(arr.getMax()) )
arr.display()
print( "\n   Adding 11, 00, 66, and 33 to make duplicates..." )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )
arr.display()
print( "\n   Eradicating dupes")
arr.a = arr.noDupes()
arr.display()
print( "\n   Adding five copies of 33..." )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.display()
print( "\n   Eradicating dupes")
arr.a = arr.noDupes()
arr.display()
print( "\n   MISSION COMPLETE!  NICE WORK SOLDIER!..." )