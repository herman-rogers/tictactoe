'''This is free software created by Boomer Rogers, distributed
   under the GNU General Public License (2013), and is intended for
   non-commercial education purposes.'''

from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *

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

class gamePlayerInput(object):

    def playerMakeMove(self, player):
        for event in pygame.event.get():
	    if board_data.boardComplete() == True and event.type == MOUSEBUTTONUP:
		load_data.soundEffect()
		userInputEndGame().reset()

            elif event.type == MOUSEBUTTONUP:
                load_data.soundEffect()
                userInputMusic().toggle()
                player_move = graphical_board.movePosition()
                if not player_move in board_data.trackMovesLeft():
                    continue
                gamePlayerMove().move(player)

            elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameExit()

class gamePlayerMove(object):

    def move(self, player):
        player_move = graphical_board.movePosition()
        board_data.makeMove(player_move, player)
        return gameComputerMove().computerMakeMove(player)

class userInputMusic(object):

    def toggle(self):
        if gameToggleMusic().toggleMusic().collidepoint(graphical_board.mouseCoords()) and pygame.mixer.music.get_busy() == 0:
            return load_data.getMusic()

	elif gameToggleMusic().toggleMusic().collidepoint(graphical_board.mouseCoords()) and pygame.mixer.get_busy():
            pygame.mixer.music.stop()

class userInputEndGame(object):

    def reset(self):

            if load_data.resetFunction().collidepoint(graphical_board.mouseCoords()):
                gameReset().dataReset()

            elif load_data.exitFunction().collidepoint(graphical_board.mouseCoords()):
                gameExit()

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

class gameToggleMusic(object):

    def toggleMusic(self):
	music_on, music_off = load_data.loadPng('musicon.png'), load_data.loadPng('musicoff.png')
	toggle = music_on.get_rect()

        if pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_on, toggle)
        if not pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_off, toggle)
        return music

class gameReset(object):

    def dataReset(self):
        board_data.all_positions = [0,0,0,0,0,0,0,0,0]
        graphical_board.generateNewBoard(80)

game_start = gameStart()

if __name__ == '__main__':
    game_start.mainGame()
