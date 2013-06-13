import sys,os

#sys.path.append("..")

from lib.loading_data.loadingdata import *
from lib.minimax_AI.minimaxAI import *
from lib.board_settings.boardsettings import *

class gamePlayerInput(object):

    def playerMakeMove(self, player):
        if board_data.boardComplete() == True and event.type == MOUSEBUTTONUP:
            load_data.soundEffect()
            userInputEndGame().reset()

            gamePlayerMove().move(player)

            elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameExit()

class gamePlayerMove(object):

    def move(self, player):

        for event in pygame.event.get():

            elif event.type == MOUSEBUTTONUP:
                userInputMusic().toggle()

            player_move = graphical_board.movePosition()
            if not player_move in board_data.trackMovesLeft():
                continue
            board_data.makeMove(player_move, player)

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

class gameToggleMusic(object):

    def toggleMusic(self):
        music_on, music_off = load_data.loadPng('musicon.png'), load_data.loadPng('musicoff.png')
        toggle = music_on.get_rect()

        if pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_on, toggle)
        if not pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_off, toggle)
        return music
