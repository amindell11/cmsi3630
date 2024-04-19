import os
import random
import time
from highScore import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showHighScore():
    print(f"High Score: {highscore} by {highName}")

def showScore():
    print(f"Score: {score}")

def addColor():
    global simonsColors
    simonsColors += random.choice(colors)
def userTurn():
    turn = input("Your Turn: \n").upper()
    return turn

colors = ('R', 'G', 'B', 'Y')
simonsColors = []
score = 0

for i in range(1):
    simonsColors += random.choice(colors)

clear()
showScore()
time.sleep(2)

while True:
    print("Simon Says: ")
    time.sleep(1)
    clear()
    showScore()
    addColor()

    addColor()
    sequence = ''.join(simonsColors)

    for color in simonsColors:
        print("Simon Says: ")
        time.sleep(.1)
        clear()
        showScore()

        print(f"Simon Says: {color}")
        time.sleep(1)
        clear()
        showScore()

    if userTurn() == sequence:
        score += 1
        clear()
        showScore()

    else:
        if score > highscore:

            clear()
            print(f"Game Over \n New High Score: {score}!")
            name = input("Enter your name: ")

            sethHghScore(name, str(score))
            break

        else:
            clear()
            print("Game Over! ")

            showHighScore()
            showScore()
            break




