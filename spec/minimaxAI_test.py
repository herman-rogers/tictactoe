import unittest, sys, os

sys.path.append("..")

from lib.game import*

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

    def testRaiseTypeErrorMakeMove(self):
        self.failUnlessRaises(TypeError, board_data.makeMove, None)

    def testMovesAreRemovedInTrackMovesLeft(self):
        moves_left = [0,1,4,5,6,7,8]
        self.assertEqual(moves_left, self.ai.trackMovesLeft())

    def testReturnCorrectXPlayerPositions(self):
        X_positions = [2]
        self.assertEqual(X_positions, self.ai.getPositions('X'))

    def testReturnCorrectOPlayerPositions(self):
        O_positions = [3]
        self.assertEqual(O_positions, self.ai.getPositions('O'))

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

    def testBoardCompleteXHasWon(self):
	self.ai.all_positions = ['X','X','X',0,0,0,0,0,0]
	self.assertTrue(self.ai.boardComplete())

    def testBoardCompleteOHasWon(self):
        self.ai.all_positions = ['O','O','O',0,0,0,0,0,0]
        self.assertTrue(self.ai.boardComplete())

    def testWinnerPlayerX(self):
	self.ai.all_positions = ['X','X','X',0,0,0,0,0,0]
	self.assertTrue(self.ai.winner() == 'X')

    def testWinnerPlayerO(self):
	board_data.all_positions = ['O','O','O',0,0,0,0,0,0]
	self.assertTrue(board_data.winner() == 'O')

class testMiniMax(unittest.TestCase):

    def testGetEnemyPlayer(self):
        player = 'X'
        self.assertEqual('O', getEnemy(player))


if __name__ == '__main__':
    unittest.main()

