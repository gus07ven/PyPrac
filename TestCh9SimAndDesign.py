from unittest import TestCase
import unittest
from Ch9_SimAndDesign import gameOver


class TestCh9SimAndDesign(TestCase):

    def testGameOver_startingGame_shouldReturnFalse(self):
        self.assertEqual(gameOver(0, 0), False)

    def testGameOver_middleOfGame_shouldReturnFalse(self):
        self.assertEqual(gameOver(5, 10), False)

    def testGameOver_endGameAWins_shouldReturnTrue(self):
        self.assertEqual(gameOver(15, 3), True)

    def testGameOver_endGameBWins_shouldReturnTrue(self):
        self.assertEqual(gameOver(3, 15), True)


if __name__ == '__main__':
    unittest.main()
