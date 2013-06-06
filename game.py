'''This is free software created by Boomer Rogers and distributed
   under the GNU General Public License (2013)and is intended for
   non-commercial education purposes.'''

from lib.board_settings.boardsettings import *
from lib.minimax_AI.minimaxAI import *

class gameStart(object):

    def mainGame(self):
        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        mainBoard = graphical_board.generateNewBoard(80)
        gamestate = True 

        while gamestate:
            player = 'X'
            self.toggleMusic()
            self.endOfGame()
            self.playerMakeMove(player, mainBoard)
            pygame.display.update()

    def playerMakeMove(self, player, mainBoard):
        for event in pygame.event.get():
            posx, posy = pygame.mouse.get_pos()

            if board_data.boardComplete() == True and event.type == MOUSEBUTTONUP:
                load_data.soundEffect()

                if load_data.resetFunction().collidepoint((posx, posy)):
                    board_data.all_positions = [0,0,0,0,0,0,0,0,0]
                    mainBoard = graphical_board.generateNewBoard(80)

                elif load_data.exitFunction().collidepoint((posx, posy)):
                    gameExit()

            elif event.type == MOUSEBUTTONUP:
                load_data.soundEffect()

                if self.toggleMusic().collidepoint((posx, posy)) and pygame.mixer.music.get_busy() == 0:
                    return load_data.getMusic()

		if self.toggleMusic().collidepoint((posx, posy)) and pygame.mixer.get_busy():
		    pygame.mixer.music.stop()

                player_move = graphical_board.movePosition(mainBoard, board_data, player)
                if not player_move in board_data.trackMovesLeft():
                    continue
                board_data.makeMove(player_move, player)
                return self.computerMakeMove(mainBoard, player)

            elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameExit()

    def computerMakeMove(self, mainBoard, player):
        pygame.display.update()
        player = getEnemy(player)
        makecomp_move = computer_move.determine(board_data, player)
        time.sleep(0.7)
        board_data.makeMove(makecomp_move, player)
        load_data.soundEffect()
        return self.playerMakeMove(mainBoard, player)

    def toggleMusic(self):
	music_on, music_off = load_data.loadPng('musicon.png'), load_data.loadPng('musicoff.png')
	toggle = music_on.get_rect()

        if pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_on, toggle)
        if not pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_off, toggle)
        return music

    def endOfGame(self):
        if board_data.boardComplete():
            if board_data.winner() == 'O':
                load_data.computerWin()
                    
            if board_data.winner() == None:
                load_data.displayDraw()
            return load_data.resetFunction() and load_data.exitFunction()
                    
game_start = gameStart()

if __name__ == '__main__':
    game_start.mainGame()
