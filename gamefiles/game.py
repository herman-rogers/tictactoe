'''This is free software created by Boomer Rogers and distributed under the GNU General Public License (2013) and is intended for non-commercial education purposes.'''

import pygame, pygame.mixer, sys, os, random, time

sys.path.insert(0, os.path.abspath(".."))

from displayset.window_settings import*
from datahandler.loadingdata import*
from computerAI.minimaxAI import getEnemy, determine, board_data
from pygame.locals import*


class gameStart(object):

    def mainGame(self):

        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        mainBoard = generateNewBoard(80)
        turn = random.choice(['computer', 'player'])
        gamestate = 1

        toggle_on = (['on'])
        music_on = load_data.loadPng('musicon.png')
        toggle_yes = music_on.get_rect()
        music_off = load_data.loadPng('musicoff.png')
        toggle_off = music_off.get_rect()
        window_set.surface.blit(music_on, toggle_yes)

        while gamestate == 1:
            player = 'X'

            if board_data.boardComplete():

                computer_win = load_data.loadPng('resetcomputerwon.png')
                display_reset = computer_win.get_rect(center=(window_set.window_width/2, window_set.window_height/2))

                play_again = load_data.loadPng('playagain.png')
                reset_yes = play_again.get_rect(center=(window_set.window_width/2 + 80,window_set.window_height/2 + 60))

                exit_game = load_data.loadPng('exitbutton.png')
                exit_yes = play_again.get_rect(center=(window_set.window_width/2 - 80, window_set.window_height/2 + 60))

                draw_game = load_data.loadPng('drawbox.png')
                display_draw = draw_game.get_rect(center=(window_set.window_width/2, window_set.window_height/2))
                    
                if board_data.winner() == 'O':
                    window_set.surface.blit(computer_win, display_reset)
                    window_set.surface.blit(play_again, reset_yes)
                    window_set.surface.blit(exit_game, exit_yes)
                    
                if board_data.winner() == None:
                    window_set.surface.blit(draw_game, display_draw)
                    window_set.surface.blit(play_again, reset_yes)
                    window_set.surface.blit(exit_game, exit_yes)

                for event in pygame.event.get():
 
                    if event.type == MOUSEBUTTONUP:
                        load_data.soundEffect()
                        spotx, spoty = pygame.mouse.get_pos()
                        if reset_yes.collidepoint((spotx, spoty)):
                            mainBoard = generateNewBoard(80)
                            window_set.surface.blit(music_on, toggle_yes)
                            board_data.all_positions = [0,0,0,0,0,0,0,0,0]

                        if exit_yes.collidepoint((spotx, spoty)):
                            gameExit()

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        gameExit()

            if turn == 'player':
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        load_data.soundEffect()
                        posx, posy = pygame.mouse.get_pos()
                        if toggle_yes.collidepoint((posx, posy)) and toggle_on == ['on']:
                            pygame.mixer.music.pause()
                            toggle_on = ['off']
                            window_set.surface.blit(music_off, toggle_off)

                        elif toggle_off.collidepoint((posx, posy)) and toggle_on == ['off']:
                            pygame.mixer.music.unpause()
                            toggle_on = ['on']
                            window_set.surface.blit(music_on, toggle_yes)

                        player_move = movePosition(mainBoard, board_data, player)
                        if not player_move in board_data.trackMovesLeft():
                            continue
                        board_data.makeMove(player_move, player)
                        turn = 'computer'

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        gameExit()

            elif turn == 'computer':
                '''Make the computer seem like it's thinking'''
                pauseUntil = time.time() + random.randint(2,5)*0.2

                while time.time() < pauseUntil:
                    pygame.display.update()

                player = getEnemy(player)
                computer_move = determine(board_data, player)
                board_data.makeMove(computer_move, player)
                load_data.soundEffect()
                turn = 'player'

            pygame.display.update()

def gameExit():
    pygame.quit()
    exit()

def movePosition(board, board_data, player):
    '''Get Board X,Y Coordinates from player and return list move'''

    posx, posy = pygame.mouse.get_pos()
    mousex, mousey = getMouseClick(board, posx, posy)
    get_list = zip(*[iter(enumerate(board_data.all_positions))]*3)
    get_matrix = map(list, zip(*get_list))

    try:
        for value in get_matrix[mousex][mousey]:
            if value in board_data.trackMovesLeft():
                load_data.drawPlayer(mousex, mousey, 0,0)
            return value
    except TypeError:
        pass

def getMouseClick(board, x, y):
    '''Converts mouse coordinates to board coordinates'''
    for tileX in range(len(board)):

        for tileY in range(len(board[0])):
            left, top = window_set.getLeftTopCoords(tileX, tileY)
            tileRect = pygame.Rect(left, top, window_set.box_size, window_set.box_size)
            
            if tileRect.collidepoint(x,y):
                return(tileX, tileY)
    return (None,None)

def drawBoard(board): 
    '''Draw the main game graphical board'''
    bg = load_data.loadPng("background2.png")
    backgroundRect = bg.get_rect()
    window_set.surface.blit(bg, backgroundRect)

    left, top = window_set.getLeftTopCoords(0,0)
    width = window_set.board_width * window_set.box_size
    height = window_set.board_height * window_set.box_size

    for tilex in range(len(board)):    
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                load_data.drawSquare(tilex, tiley, board[tilex][tiley])

def getStartBoard():

    counter = 1
    board = []
    for x in range(window_set.board_width):
	column = []
	for y in range(window_set.board_height):
	    column.append(counter)
	    counter += window_set.board_width
	board.append(column)
	counter -= window_set.board_width * (window_set.board_height - 1) + window_set.board_width - 1
    return board

def generateNewBoard(self):
    board = getStartBoard()
    drawBoard(board)
    pygame.display.update()
    return (board)

if __name__ == '__main__':
    load_data.getMusic()
    game_start.mainGame()

game_start = gameStart()

