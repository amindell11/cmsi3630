###
# filename: Card.py
# purpose:  simulation of a deck of playing cards
# author:   Dr. Johnson
# date:     2023-01-07
###

class Card:
   suits = { "S", "H", "D", "C" }       # spades, hearts, diamonds, clubs
   ranks = [0, 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

   def __init__( self, suit, value ):
#      thisSet = { "?", "?", "?", "?" }      # can also do it with ASCII art
      if((suit not in Card.suits)):
         print( "   Illegal suit value sent to initializer." )
      elif( 1 > value or 13 < value ):
         print( "   Illegal card rank sent to initilaizer>" )
      else:
         self.value = value
         self.cardSuit = suit
         self.cardRank = Card.ranks[value]

   def __str__( self ):
      rep = "[{},{}]".format(str(self.cardSuit), str(self.cardRank))
      return rep
   def __repr__(self):
        return repr((self.value, self.cardSuit, self.cardRank))
