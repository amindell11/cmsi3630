###
# filename: Card.py
# purpose:  simulation of a poker hand
# author:   Dr. Johnson
# date:     2023-01-07
###
from enum import Enum
from Card import Card
class HandRankings(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.rank = Hand.calculate_hand_value(self)
    def __str__(self):
        return  self.cards.__str__()
    @staticmethod
    def calculate_hand_value(hand):
        # Placeholder for the logic to calculate the hand's value
        # This should analyze the cards list and return the appropriate HandRankings value
        # For now, it just returns HIGH_CARD as a placeholder
        hand.sort()
        return HandRankings.HIGH_CARD
    

    def sort(self):
        self.cards.sort(key=lambda card: card.value)
        return HandRankings.HIGH_CARD
    @staticmethod
    def isHandHighCard(sle):
        pass
cards = [Card("S",3),Card("H",1),Card("C",2)]  # Example cards, you need to define the format
hand = Hand(cards)
print(hand)

print(hand.rank)
