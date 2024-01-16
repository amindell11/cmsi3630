import math
import random
#generates a possible hand and determines if it is blackjack
def generateBlackjackHand():
    a = int(random.randrange(2,15))
    b = int(random.randrange(2,15))
    if(a!=11):
        if(a>10): a = 10
    if(b!=11):
        if(b>10): b = 10
    return a+b==21
def dartThrow( inHits):
    if(generateBlackjackHand()):
        return inHits + 1
    else:
        return inHits
def main():
    hits = 0
    numDarts = int(input("\n number of darts to throw:" ))
    for i in range(numDarts):
        hits = dartThrow(hits)
    approxPi =(float(hits)/float(numDarts))
    print("\n Real Valueof BJ: ",float(100* 32/663))
    print(" Approximation of BJ: ", 100* approxPi)
main()
