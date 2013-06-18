import unittest, sys
from mock import patch, Mock

sys.path.append("..")
from lib.player_move.playermove import *

class testComputerAndPlayerMakingMoves(unittest.TestCase):
    def setUp(self):
        pygame.mixer.init()
        self.computer = 'O'
        self.player = 'X'
        self.player_move = gamePlayerInput()

    @patch('lib.minimax_AI.minimaxAI.AI.makeMove')
    def testValuesThatReturnWhenComputerMakesMoves(self, mock_computer_move):
        comp_move = gameComputerMove()
        comp_move.computerMakeMove(self.computer)
        self.assertTrue(mock_computer_move.called)

    @patch('lib.loading_data.loadingdata.load_data.soundEffect')
    def testWhenComputerMakesMoveSoundEffectsPlay(self, mock_computer_sound):
        comp_soundfx = gameComputerMove()
        comp_soundfx.computerMakeMove(self.computer)
        self.assertTrue(mock_computer_sound.called)

    @patch('lib.player_move.playermove.gamePlayerInput.playerMakeMove')
    def testGamePlayerTurnIsReturned(self, mock_player_turn):
        player_turn = gamePlayerTurn()
        player_turn.playerTurn()
        self.assertTrue(mock_player_turn.called)

    @patch('lib.player_move.playermove.gameComputerMove.computerMakeMove')
    def testGameComputerTurnIsReturned(self, mock_computer_turn):
        get_turn.turn = False
        get_turn.playerTurn()
        self.assertTrue(mock_computer_turn.called)

    @patch('lib.player_move.playermove.userInputMusic.toggle')
    def testPlayerInputTogglesMusic(self, mock_player_toggle):
        pygame.event.post(pygame.event.Event(MOUSEBUTTONUP))
	self.player_move.playerMakeMove(self.player)
	self.assertTrue(mock_player_toggle.called)

    @patch('lib.loading_data.loadingdata.load_data.soundEffect')
    def testPlayerInputMakesSoundEffect(self, mock_player_sound):
        pygame.event.post(pygame.event.Event(MOUSEBUTTONUP))
	self.player_move.playerMakeMove(self.player)
	self.assertTrue(mock_player_sound.called)

    @patch('lib.board_settings.boardsettings.createGraphicalBoard.movePosition')
    def testPlayerMakeMoveIsRecorded(self, mock_player_position):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        board_data.trackMovesLeft() == [0,1,2,3,4,5,6,7,8]
        for move in board_data.trackMovesLeft():
            board_data.makeMove(move, 0)
        pygame.event.post(pygame.event.Event(MOUSEBUTTONUP))
        self.player_move.playerMakeMove(self.player)
        self.assertTrue(mock_player_position.called)

    @patch('lib.player_move.playermove.userInputEndGame.reset')
    def testEndOfGameShowsOptionsForResetToPlayer(self, mock_player_reset):
	for move in board_data.trackMovesLeft():
	    board_data.makeMove(move, 'X')
	pygame.event.post(pygame.event.Event(MOUSEBUTTONUP))
	self.player_move.playerMakeMove(self.player)
	self.assertTrue(mock_player_reset.called)

if __name__ == '__main__':
    unittest.main()
