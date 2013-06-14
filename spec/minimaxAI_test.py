import unittest, sys, os

sys.path.append("..")
from lib.minimax_AI.minimaxAI import *

class testBoardDataStructure(unittest.TestCase):

    def setUp(self):
        self.ai = board_data

    def testBoardDataStartsEmpty(self):
        start_data = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(start_data, self.ai.all_positions)

    def testBeginningMoves(self):
        start_moves = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(start_moves, self.ai.trackMovesLeft())

    def testMakeMovePlayer1(self):
	test_move = [0,0,'X',0,0,0,0,0,0]
	board_data.makeMove(2,'X')
	self.assertEqual(test_move, self.ai.all_positions)

    def testMakeMovePlayer2(self):
	test_move = [0,0,'X','O',0,0,0,0,0]
	board_data.makeMove(3,'O')
	self.assertEqual(test_move, self.ai.all_positions)

    def testMovesAreRemovedInTrackMovesLeft(self):
        moves_left = [0,1,4,5,6,7,8]
        self.assertEqual(moves_left, self.ai.trackMovesLeft())

    def testReturnCorrectXPlayerPositions(self):
        self.assertEqual([2], self.ai.getPositions('X'))

    def testReturnCorrectOPlayerPositions(self):
        self.assertEqual([3], self.ai.getPositions('O'))

    def testRaiseTypeErrorMakeMove(self):
        self.assertRaises(TypeError, self.ai.makeMove, None)

class testBoardWinLoseDrawConditions(unittest.TestCase):

    def setUp(self):
        self.ai = board_data

    def testWinnerDefaultToNone(self):
        self.assertEqual(self.ai.winner(), None)

    def testBoardNotCompleteIfMovesLeft(self):
        self.ai.all_positions = [0,0,0,0,0,0,0,0]
        self.assertFalse(board_data.boardComplete())

    def testGameIsDraw(self):
	self.ai.all_positions = ['O','X','O','X','O','X','X','O','X']
	self.assertTrue(self.ai.boardComplete())

    def testWinnerPlayerX(self):
	self.ai.all_positions = ['X','X','X',0,0,0,0,0,0]
	self.assertTrue(self.ai.winner() == 'X')

    def testWinnerPlayerO(self):
	self.ai.all_positions = ['O','O','O',0,0,0,0,0,0]
	self.assertTrue(self.ai.winner() == 'O')

class testMiniMax(unittest.TestCase):

    def setUp(self):
        self.ai = board_data
        self.player = 'O'

    def testEnemyWonReturnNegativeValue(self):
        self.ai.all_positions = ['X','X','X',0,0,0,0,0,0]
        self.assertEqual(-1, self.ai.miniMax(self.ai, self.player, -2, 2))

    def testComputerWinReturnPositiveValue(self):
        self.ai.all_positions = ['O','O','O',0,0,0,0,0,0]
        self.assertEqual(1, self.ai.miniMax(self.ai, self.player, -2, 2))

    def testDrawIsReturned(self):
        self.ai.all_positions = ['O','X','O','X','O','X','X','O','X']
        self.assertEqual(0, self.ai.miniMax(self.ai, self.player, -2, 2))

    def testPlayMoveThatAvoidsLoss(self):
        self.ai.all_positions = ['X','X',0,0,'O',0,0,0,0]
        self.assertEqual(0, self.ai.miniMax(self.ai, self.player, -2, 2))

    def testPlayMovethatLeadsToWin(self):
        self.ai.all_positions = ['X','X',0,0,'O','O',0,0,0]
        self.assertEqual(1, self.ai.miniMax(self.ai, self.player, -2, 2))

class testDetermine(unittest.TestCase):

    def setUp(self):
        self.ai = board_data
        self.computermove = computer_move
        self.player = 'O'

    def testFirstMoveTakeCenter(self):
        self.ai.all_positions = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(4, self.computermove.determine(self.ai, self.player))

    def testMakeBestMove(self):
        self.ai.all_positions = ['X','X',0,0,'O',0,0,0,0]
        self.assertEqual(2, self.computermove.determine(self.ai, self.player))

    def testReturnNoneWhenChoicesListIsEmpty(self):
        self.ai.all_positions = []
        self.assertEqual(None, self.computermove.determine(self.ai, self.player))

    def testCurrentPlayerIsXGetPlayerO(self):
        self.assertEqual('X', getEnemy(self.player))

if __name__ == '__main__':
    unittest.main()
