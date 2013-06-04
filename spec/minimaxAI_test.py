import unittest, sys, os

sys.path.append("..")

from lib.game import*

class testBoardDataStructure(unittest.TestCase):

    def testBoardDataStartsEmpty(self):
        start_data = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(start_data, board_data.all_positions)

    def testBeginningMoves(self):
        start_moves = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(start_moves, board_data.trackMovesLeft())

    def testMovesAreRemovedInTrackMovesLeft(self):
        moves_left = [2,3,4,6,8]
        board_data.all_positions = ['O','X',0,0,0,'X',0,'O',0]
        self.assertEqual(moves_left, board_data.trackMovesLeft())

    def testReturnCorrectXPlayerPositions(self):
        get_player = 'X'
        board_data.all_positions = ['O','X',0,0,0,'X',0,'O',0]
        X_positions = [1,5]
        self.assertEqual(X_positions, board_data.getPositions(get_player))

    def testReturnCorrectOPlayerPositions(self):
        get_player = 'O'
        board_data.all_positions = ['O','X',0,0,0,'X',0,'O',0]
        O_positions = [0,7]
        self.assertEqual(O_positions, board_data.getPositions(get_player))

    def testMakeMovePlayerX(self):
        board_data.all_positions = ['O','X',0,0,0,'X',0,'O',0]
        test_move = ['O','X',0,'X',0,'X',0,'O',0]
        board_data.makeMove(3,'X')
        self.assertEqual(test_move, board_data.all_positions)

    def testMakeMovePlayerO(self):
        board_data.all_positions = ['O','X',0,0,0,'X',0,'O',0]
        test_move = ['O','X',0,'O',0,'X',0,'O',0]
        board_data.makeMove(3,'O')
        self.assertEqual(test_move, board_data.all_positions)

    def testRaiseTypeErrorMakeMove(self):
        self.failUnlessRaises(TypeError, board_data.makeMove, None)

class testBoardWinLoseDrawConditions(unittest.TestCase):

    def testWinnerDefaultToNone(self):
        self.assertEqual(board_data.winner(), None)

    def testBoardCompleteDefaultsFalse(self):
        self.assertFalse(board_data.boardComplete())

    def testMovesAvailableIsTracked(self):
        board_data.all_positions = [0,0]
        self.assertFalse(board_data.boardComplete())

    def testGameIsDraw(self):
        board_data.all_positions = ['X','X','O','X','X','O','O','O','X']
        self.assertTrue(board_data.boardComplete())

    def testBoardCompleteXHasWon(self):
        board_data.all_positions = ['X','X','X',0,0,0,0,0,0]
        self.assertTrue(board_data.boardComplete())

    def testWinnerPlayerX(self):
        board_data.all_positions = ['X','X','X',0,'O',0,0,0,'O']
        self.assertTrue(board_data.winner() == 'X')

    def testWinnerPlayerO(self):
        board_data.all_positions = ['O','O','O',0,'X','X',0,0,0]
        self.assertTrue(board_data.winner() == 'O')

    def testGetEnemyPlayer(self):
        player = 'X'
        self.assertEqual('O', getEnemy(player))


if __name__ == '__main__':
    unittest.main()

