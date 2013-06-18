'''This is free software created by Boomer Rogers, distributed
   under the GNU General Public License (2013), and is intended for
   non-commercial education purposes.'''
from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *
from lib.player_move.playermove import *

class gameFunction(object):

    def __init__(self):
        gameReset().dataReset()

    def mainLoop(self):
        while 1:
            get_turn.playerTurn()
            gameEnd().endOfGame()

class gameEnd(object):

    def __init__(self):
        pygame.display.update()
        window_set.clock.tick(30)
        gameToggleMusic().toggleMusic()

    def endOfGame(self):
        if board_data.boardComplete():
            if board_data.winner() == 'O':
                load_data.displayWinImage()
            else:
                load_data.displayDrawImage()        
            load_data.resetFunction() and load_data.exitFunction()

class gameReset(object):
    
    def dataReset(self):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        graphical_board.generateNewBoard(80)

if __name__ == '__main__':
    pygame.init() and pygame.display.set_caption('Tic-Tac-Toe')
    gameFunction().mainLoop()
