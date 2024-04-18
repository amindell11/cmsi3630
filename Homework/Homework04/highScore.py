def getHighScore():
    with open("highScore.txt", "r") as hs:
        stats = hs.readlines()
        return stats

def sethHghScore(name, score):
    with open("highScore.txt", "w") as hs:
        hs.write(name)
        hs.write("\n")
        hs.write(score)

record = getHighScore()
highName = record[0]
highscore = int(record[1])


