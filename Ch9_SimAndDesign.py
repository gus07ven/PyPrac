from random import random

# Print an Introduction
# Get the inputs: probA, probB, n
# Simulate n games of racquetball using probA and probB
# Print a report on the wins for playerA and playerB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def gameOver(a,b):
    # a and b represent scores for a racquetball game
    # RETURNS true if the game is over, false otherwise.
    return a == 15 or b == 15


if __name__ == '__main__':
    main()