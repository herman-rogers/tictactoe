'''This is free software created by Boomer Rogers, distributed
   under the GNU General Public License (2013), and is intended for
   non-commercial education purposes.'''

from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *
from lib.player_move.playermove import *


class gameStart(object):

    pygame.init()
    pygame.display.set_caption('Tic-Tac-War')

    def mainGame(self):
        graphical_board.generateNewBoard(80)
        return gameMainLoop().gameLoop()

class gameMainLoop(object):

    def gameLoop(self):
        while True:
            player = 'X'
            gameToggleMusic().toggleMusic()
            gamePlayerInput().playerMakeMove(player)
            gameCheckConditions().checkBoard()

class gameComputerMove(object):

    def computerMakeMove(self, player):
        pygame.display.update()
        player = getEnemy(player)
        makecomp_move = computer_move.determine(board_data, player)
        time.sleep(0.7)
        board_data.makeMove(makecomp_move, player)
        load_data.soundEffect()
        return gamePlayerInput().playerMakeMove(player)

class gameCheckConditions(object):

    def checkBoard(self):
        gameEnd().endOfGame()
        pygame.display.update()
        window_set.clock.tick(30)

class gameEnd(object):

    def endOfGame(self):
        if board_data.boardComplete():
            if board_data.winner() == 'O':
                load_data.computerWin()
                    
            if board_data.winner() == None:
                load_data.displayDraw()
            return load_data.resetFunction() and load_data.exitFunction()

class gameReset(object):

    def dataReset(self):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        graphical_board.generateNewBoard(80)

game_start = gameStart()

if __name__ == '__main__':
    game_start.mainGame()
