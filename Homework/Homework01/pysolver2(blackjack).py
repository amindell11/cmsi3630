import math
import random
def getRandomPointDistance():
    a = random.random()
    b = random.random()
    c = math.sqrt((a*a)+(b*b))
    return c

def dartThrow( inHits):
    if(getRandomPointDistance() <1.0):
        return inHits + 1
    else:
        return inHits
def main():
    hits = 0
    numDarts = int(input("\n number of darts to throw:" ))
    for i in range(numDarts):
        hits = dartThrow(hits)
    approxPi = 4*(float(hits)/float(numDarts))
    print("\n Real Valueof Pi: ",math.pi)
    print(" Approximation of PI: ", approxPi)
main()
