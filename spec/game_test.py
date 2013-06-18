import unittest, sys
from mock import patch, Mock

sys.path.append("..")

from game import *

class testMainGameWhileLoop(unittest.TestCase):

    def setUp(self):
        pygame.mixer.init()
        self.data = board_data
        self.moves_left = self.data.trackMovesLeft()

    @patch('lib.board_settings.boardsettings.createGraphicalBoard.generateNewBoard')
    def testGameFunctionInitReturnsNewBoardAtStart(self, mock_start_board):
        get_start_board = gameFunction()
        get_start_board.__init__()
        self.assertTrue(mock_start_board.called)

    @patch('lib.board_settings.boardsettings.loadMedia.resetFunction')
    def testResetButtonShowsInTheDialogAtEndOfGame(self, mock_reset_button):
        for move in self.moves_left:
            self.data.makeMove(move, 'X')
        gameEnd().endOfGame()
        self.assertTrue(mock_reset_button.called)

    @patch('lib.board_settings.boardsettings.loadMedia.resetFunction')        
    def testExitButtonShowsInTheDialogAtEndOfGame(self, mock_exit_button):
        gameEnd().endOfGame()
        self.assertTrue(mock_exit_button.called)

    @patch('lib.loading_data.loadingdata.loadMedia.displayDrawImage')
    def testDrawGameDialogIsDisplayed(self, mock_reset_dialog):
        for move in self.moves_left:
            self.data.makeMove(move,'X')
	get_game_reset = gameEnd()
	get_game_reset.endOfGame()
	self.assertTrue(mock_reset_dialog.called)

    @patch('lib.loading_data.loadingdata.loadMedia.displayWinImage')
    def testEndOfGameComputerWinReturnsCorrectScreen(self, mock_win):
        self.moves_left = [0,1,2,3,4,5,6,7,8]
        for move in self.moves_left:
            self.data.makeMove(move, 'O')
        get_game_win = gameEnd()
        get_game_win.endOfGame()
        self.assertTrue(mock_win.called)

    @patch('lib.board_settings.boardsettings.createGraphicalBoard.generateNewBoard')
    def testGameReturnsNewBoardAfterGameEnds(self, mock_end_board):
        get_reset_board = gameReset()
        get_reset_board.dataReset()
        self.assertTrue(mock_end_board.called)

    def testGameReturnEmptrDataStuctureAfterGameEnds(self):
        gameReset().dataReset()
        empty_structure = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(self.data.all_positions, empty_structure)

if __name__ == '__main__':
    unittest.main()
