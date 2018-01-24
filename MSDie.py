# Class definition for an n-sided die.
from random import randrange

class MSDie:

    def __init__(self, numSides):
        self.numSides = numSides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.numSides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


