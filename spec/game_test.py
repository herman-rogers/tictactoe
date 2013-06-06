import unittest, sys

sys.path.append("..")

from game import *

class testGameStart(unittest.TestCase):

    def setUp(self):
        self.main_game = game_start
        self.game_data = board_data
        self.player = 'X'

    def testEndOfGameComputerWin(self):
        self.game_data.boardComplete() == False
        self.assertEqual(None, self.main_game.endOfGame())

if __name__ == '__main__':
    unittest.main()
