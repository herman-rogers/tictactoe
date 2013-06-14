import unittest, sys
from mock import patch, Mock

sys.path.append("..")

from game import *

class testMainGameWhileLoop(unittest.TestCase):

    @patch('lib.board_settings.boardsettings.createGraphicalBoard.generateNewBoard')
    def testGameFunctionInitReturnsNewBoardAtStart(self, mock_start_board):
        get_start_board = gameFunction()
        get_start_board.__init__()
        self.assertTrue(mock_start_board.called)

#    @patch('lib.player_move.playermove.gamePlayerInput.playerMakeMove')
    #def testGameFunctionMainLoopReturnsPlayerMoveAtStart(self, mock_player_turn):
        #get_player_move = gameFunction()
        #get_player_move.mainLoop()
        #self.assertTrue(mock_player_turn.called)

class testEndOfGameAndResetPrompts(unittest.TestCase):

    def setUp(self):
        board_data.all_positions = [0]

    @patch('lib.loading_data.loadingdata.loadMedia.resetFunction')
    def testResetButtonShowsAtEndOfGame(self, mock_reset_button):
        reset_button = gameEnd()
        reset_button.endOfGame()
        self.assertTrue(mock_reset_button.called)
        restore()

    @patch('lib.board_settings.boardsettings.createGraphicalBoard.generateNewBoard')
    def testGameReturnsNewBoardAfterEndGame(self, mock_end_board):
        get_reset_board = gameReset()
        get_reset_board.dataReset()
        self.assertTrue(mock_end_board.called)

   # @patch() THIS IS SAVED TO TEST DATARESET BOARD ALL_POSITIONS



if __name__ == '__main__':
    unittest.main()
