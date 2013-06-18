from game import *
from lib.loading_data.loadingdata import *
from lib.minimax_AI.minimaxAI import *
from lib.board_settings.boardsettings import *

class gamePlayerTurn(object):

    def __init__(self):
        self.turn = True
        self.player = 'X'

    def playerTurn(self):
        player = self.player
        if self.turn:
            return gamePlayerInput().playerMakeMove(player)
        return gameComputerMove().computerMakeMove(player)
get_turn = gamePlayerTurn()

class gamePlayerInput(object):

    def playerMakeMove(self, player):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                load_data.soundEffect()
                userInputMusic().toggle()
                if board_data.boardComplete() == True:
                    userInputEndGame().reset()
                else:
                    player_move = graphical_board.movePosition()
                    if not player_move in board_data.trackMovesLeft():
                        continue
                    board_data.makeMove(player_move, player)
                    get_turn.turn = False
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameExit()

class gameComputerMove(object):

    def computerMakeMove(self, player):
        player = getEnemy(player)
        makecomp_move = computer_move.determine(board_data, player)
        time.sleep(0.7)
        board_data.makeMove(makecomp_move, player)
        load_data.soundEffect()
        get_turn.turn = True

class gameToggleMusic(object):

    def toggleMusic(self):
        music_on, music_off = load_data.loadPng('musicon.png'), load_data.loadPng('musicoff.png')
        toggle_switch = music_on.get_rect()
        if pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_on, toggle_switch)
        if not pygame.mixer.music.get_busy():
            music = window_set.surface.blit(music_off, toggle_switch)
        return music

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
