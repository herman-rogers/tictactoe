'''This is free software created by Boomer Rogers, distributed
   under the GNU General Public License (2013), and is intended for
   non-commercial education purposes.'''

from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *
from lib.player_move.playermove import *

class gameFunction(object):

    def __init__(self):
        graphical_board.generateNewBoard(80)

    def mainLoop(self):
        while True:
            player = 'X'
            gamePlayerInput().playerMakeMove(player)
            gameEnd().endOfGame()

class gameEnd(object):

    def __init__(self):
        pygame.display.update()
        window_set.clock.tick(30)

    def endOfGame(self):
        if board_data.boardComplete():
            if board_data.winner() == 'O':
                load_data.displayWinImage()
                    
            if board_data.winner() == None:
                load_data.displayDrawImage()
            load_data.resetFunction() and load_data.exitFunction()

class gameReset(object):
    
    def dataReset(self):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        graphical_board.generateNewBoard(80)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tic-Tac-War')
    gameFunction().mainLoop()
