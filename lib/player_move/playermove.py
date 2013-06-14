from game import *
from lib.loading_data.loadingdata import *
from lib.minimax_AI.minimaxAI import *
from lib.board_settings.boardsettings import *

class gamePlayerInput(object):

    def playerMakeMove(self, player):

        gameToggleMusic().toggleMusic()
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
                board_data.makeMove(player_move, player)
                return gameComputerMove().computerMakeMove(player)

            elif event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
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

class userInputMusic(object):

    def toggle(self):
        if gameToggleMusic().toggleMusic().collidepoint(graphical_board.mouseCoords()) and pygame.mixer.music.get_busy() == 0:
            return load_data.getMusic()
        elif gameToggleMusic().toggleMusic().collidepoint(graphical_board.mouseCoords()) and pygame.mixer.get_busy():
            pygame.mixer.music.stop()

class gameToggleMusic(object):

    def toggleMusic(self):
        music_on, music_off = load_data.loadPng('musicon.png'), load_data.loadPng('musicoff.png')
        toggle_switch = music_on.get_rect()
        if pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_on, toggle_switch)
        if not pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_off, toggle_switch)
        return music

class userInputEndGame(object):

    def reset(self):
            if load_data.resetFunction().collidepoint(graphical_board.mouseCoords()):
                gameReset().dataReset()
            elif load_data.exitFunction().collidepoint(graphical_board.mouseCoords()):
                gameExit()
