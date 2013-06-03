import unittest, sys, os

sys.path.insert(0, os.path.abspath(".."))

from gamefiles.game import*

class testIfImagesLoadCorrectly(unittest.TestCase):

    def testImageExists(self):
        image = load_data.loadPng("computer.png")
        self.assertTrue(image)

    def testImageException(self):
        self.failUnlessRaises(SystemExit, load_data.loadPng, "penguine.png")

class testBoardDataStructure(unittest.TestCase):

    def testBoardDataStartsEmpty(self):
        start_data = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(start_data, board_data.all_positions)

    def testBeginningMoves(self):
        start_moves = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(start_moves, board_data.trackMovesLeft())

    def testXPlayerPositions(self):
        get_player = 'X'
        board_data.all_positions = ['X',0,0,'O','X','X',0,'O',0]
        X_positions = [0,4,5]
        self.assertEqual(X_positions, board_data.getPositions(get_player))

    def testOPlayerPositions(self):
        get_player = 'O'
        board_data.all_positions = [0,0,'O','X','O','X', 0,0,'O']
        O_positions = [2,4,8]
        self.assertEqual(O_positions, board_data.getPositions(get_player))

class testBoardWinLoseDrawConditions(unittest.TestCase):

    def testWinnerDefaultToNone(self):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(board_data.winner(), None)

    def testMovesAvailableIsTracked(self):
        board_data.all_positions = [0,0]
        self.assertFalse(board_data.boardComplete())

    def testBoardCompleteDefaultsFalse(self):
        self.assertFalse(board_data.boardComplete())

    def testBoardWinnerDefaultsNone(self):
        self.assertEqual(board_data.winner(), None)

    def testGameIsDraw(self):
        board_data.all_positions = ['X','X','O','X','X','O','O','O','X']
        self.assertTrue(board_data.boardComplete())

    def testPlayerXHasWon(self):
        board_data.all_positions = ['X','X','X',0,0,0,0,0,0]
        self.assertTrue(board_data.winner() == 'X')

    def testPlayerOHasWon(self):
        board_data.all_positions = ['O','O','O',0,'X','X',0,0,0]
        self.assertTrue(board_data.winner() == 'O')

    def testGetEnemyPlayer(self):
        player = 'X'
        self.assertEqual('O', getEnemy(player))


if __name__ == '__main__':
    unittest.main()

