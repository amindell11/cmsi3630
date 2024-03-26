import math

for row in range( 100 ):
    waveHeight = math.fabs(math.exp(row/20))
    numberOfStars = int( round( waveHeight, 0 ) )
    if(numberOfStars>50):
           break
    for col in range( numberOfStars ):
        print("*", end = "" )
    print()
