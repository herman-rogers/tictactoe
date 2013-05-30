'''This is free software created by Herman Rogers and distributed under the GNU General Public License (2013) and is intended for non-commercial education purposes.'''

import pygame, pygame.mixer, sys, os, random, time, itertools, operator 
from pygame.locals import*
from itertools import*

WINDOWWIDTH, WINDOWHEIGHT = 1280, 720 #854, 480
BOARDWIDTH = 3
BOARDHEIGHT = 3
BOXSIZE = 130
XSIZE = 130
 
#Color Index -- Changing these values changes the colors
#          R   G   B

BLACK = ((0,0,0))

TILECOLOR = BLACK

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def mainGame():
        global FPSCLOCK, SURFACE
        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        mainBoard = generateNewBoard(80)
        board_data = AI()
        turn = random.choice(['computer', 'player'])
        toggle_on = (['on'])
        gamestate = 1
        music_on = load_png('musicon.png')
        toggle_yes = music_on.get_rect()
        music_off = load_png('musicoff.png')
        toggle_off = music_off.get_rect()
        SURFACE.blit(music_on, toggle_yes)

        while gamestate == 1:
            player = 'X'

            #Options and prompts for when the game is over.
            if board_data.boardComplete():

                computer_win = load_png('resetcomputerwon.png')
                display_reset = computer_win.get_rect(center=(WINDOWWIDTH/2, WINDOWHEIGHT/2))

                play_again = load_png('playagain.png')
                reset_yes = play_again.get_rect(center=(WINDOWWIDTH/2 + 80,WINDOWHEIGHT/2 + 60))

                exit_game = load_png('exitbutton.png')
                exit_yes = play_again.get_rect(center=(WINDOWWIDTH/2 - 80, WINDOWHEIGHT/2 + 60))

                draw_game = load_png('drawbox.png')
                display_draw = draw_game.get_rect(center=(WINDOWWIDTH/2, WINDOWHEIGHT/2))
                    
                if board_data.winner() == 'O':
                    SURFACE.blit(computer_win, display_reset)
                    SURFACE.blit(play_again, reset_yes)
                    SURFACE.blit(exit_game, exit_yes)
                    
                if board_data.winner() == None:
                    SURFACE.blit(draw_game, display_draw)
                    SURFACE.blit(play_again, reset_yes)
                    SURFACE.blit(exit_game, exit_yes)

                for event in pygame.event.get():
 
                    if event.type == MOUSEBUTTONUP:
                        soundEffect()
                        spotx, spoty = pygame.mouse.get_pos()
                        if reset_yes.collidepoint((spotx, spoty)):
                            mainBoard = generateNewBoard(80)
                            SURFACE.blit(music_on, toggle_yes)
                            board_data.all_positions = [0,0,0,0,0,0,0,0,0]

                        if exit_yes.collidepoint((spotx, spoty)):
                            gameExit()

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        gameExit()

            if turn == 'player':
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        soundEffect()
                        posx, posy = pygame.mouse.get_pos()
                        if toggle_yes.collidepoint((posx, posy)) and toggle_on == ['on']:
                            pygame.mixer.music.pause()
                            toggle_on = ['off']
                            SURFACE.blit(music_off, toggle_off)

                        elif toggle_off.collidepoint((posx, posy)) and toggle_on == ['off']:
                            pygame.mixer.music.unpause()
                            toggle_on = ['on']
                            SURFACE.blit(music_on, toggle_yes)

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
                soundEffect()
                turn = 'player'

	    pygame.display.update()

class AI(object):
    '''Class for determining both player and computer moves'''
    winning_moves = (
              [0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6],
                    )

    winners = ('X-win', 'Draw', 'O-win')

    ##Board Data Structure (Different from Graphical Structure)
    def __init__(self, all_positions=[]):
        if len(all_positions) == 0:
            self.all_positions = [0 for i in range(9)]
        else:
            self.all_positions = all_positions

    def trackMovesLeft(self):
        return [k for k, v in enumerate(self.all_positions) if v is 0]

    def availableCombos(self, player):
        return self.trackMovesLeft() + self.getPositions(player)

    def boardComplete(self):
        if 0 not in [v for v in self.all_positions]:
            return True
        if self.winner() != None:
            return True
        return False

    def xWon(self):
        return self.winner() == 'X'

    def oWon(self):
        return self.winner() == 'O'

    def draw(self):
        return self.boardComplete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.getPositions(player)
            for combo in self.winning_moves:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def getPositions(self, player):
        return [k for k, v in enumerate(self.all_positions) if v == player]

    def makeMove(self, position, player):
        try:
            self.all_positions[position] = player
        except TypeError:
            pass

    def miniMax(self, node, player, alpha, beta):
        if node.boardComplete():
            if node.xWon():
                return -1
            elif node.draw():
                return 0
            elif node.oWon():
                return 1

        for move in node.trackMovesLeft():
            node.makeMove(move, player)
            variable = self.miniMax(node, getEnemy(player), alpha, beta)
            node.makeMove(move, 0)

            if player == 'O':
                if variable > alpha:
                    alpha = variable
                if alpha >= beta:
                    return beta
            else:
                if variable < beta:
                    beta = variable
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta

def determine(board_data, player):
    a = -2
    choices = []
    make_coords = list(product(range(3), repeat =2 ))

    if len(board_data.trackMovesLeft()) == 9:
	posx, posy = make_coords[4]
	drawComputer(posy, posx, 0)
        return 4

    for move in board_data.trackMovesLeft():
        board_data.makeMove(move, player)
        variable = board_data.miniMax(board_data, getEnemy(player), -2, 2)
        board_data.makeMove(move, 0)
      #  print 'move:', move + 1, 'causes:', board_data.winners[variable] ##uncomment for debugging
        if variable > a:
            a = variable
            choices = [move]
        elif variable == a:
            choices.append(move)

    try:
        choose_move = random.choice(choices)
        posx,posy = make_coords[choose_move]
        drawComputer(posy, posx, 0)
        return choose_move
    except IndexError:
        pass

def getEnemy(player):
    if player == 'X':
        return 'O'
    return 'X'

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
                drawPlayer(mousex, mousey, 0,0)
            return value
    except TypeError:
        pass
   # print 'You can\'t move there, Captain' ##Uncomment for debugging

def getMouseClick(board, x, y):
    '''Converts mouse coordinates to board coordinates'''
    for tileX in range(len(board)):

        for tileY in range(len(board[0])):
            left, top = getLeftTopCoords(tileX, tileY)
            tileRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            
            if tileRect.collidepoint(x,y):
                return(tileX, tileY)
    return (None,None)

def getLeftTopCoords(tileX, tileY):
    left = XMARGIN + (tileX * BOXSIZE) + (tileX - 1)
    top = YMARGIN + (tileY * BOXSIZE) + (tileY - 1)
    return (left, top) 

def drawBoard(board): 
    '''Draw the main game graphical board'''
    bg = load_png("background2.png")
    backgroundRect = bg.get_rect()
    SURFACE.blit(bg, backgroundRect)
    left, top = getLeftTopCoords(0,0)
    width = BOARDWIDTH * BOXSIZE
    height = BOARDHEIGHT * BOXSIZE

    for tilex in range(len(board)):    
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawSquare(tilex, tiley, board[tilex][tiley])

def getStartBoard():
    #Returns Values for Tile Positioning (separate from data structure)
    #[1,4,7], [2,5,8],[3,6,9]
 
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1
    return board

def generateNewBoard(self):
    board = getStartBoard()
    drawBoard(board)
    pygame.display.update()
    return (board)

## Images and image Handling are stored here

def drawPlayer(tilex, tiley, number, adjx = 0, adjy = 0):

    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65
 
    penguine_image = load_png("player.png")
    resizePenguine = pygame.transform.scale(penguine_image, (XSIZE, XSIZE))
    SURFACE.blit(resizePenguine, (left + adjx, top + adjy))

def drawComputer(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65
 
    penguine_image = load_png("computer.png")
    resizePenguine = pygame.transform.scale(penguine_image, (XSIZE, XSIZE))
    SURFACE.blit(resizePenguine, (left + adjx, top + adjy))

def drawSquare(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley,) 
    pygame.draw.rect(SURFACE, TILECOLOR, (left + adjx, top + adjy, BOXSIZE, BOXSIZE))

def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('data/sounds/skye.ogg')
    pygame.mixer.music.play(-1)

def soundEffect():
    sound_effect = load_sound('soundeffect.ogg')
    sound_effect.set_volume(0.5)
    sound_effect.play()

def load_png(name):
    """This is so we can load objects relative paths"""

    fullname = os.path.join('data/images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Seems like I lost your image:', fullname
        raise SystemExit, message
    return image

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data/sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('%s Music Not Found!' % fullname)
	raise SystemExit(str(geterror()))
    return sound

##################STARTING FUNCTION###################

if __name__ == '__main__':
    startMusic()
    mainGame()

#def randomComputerAI(all_positions):
    '''This is for an easy AI option, left in for future implementations'''

#    posx, posy = random.randint(0,2), random.randint(0,2)
    #computer_move = False
 
    #if computer_move == False:
	#if all_positions[posy][posx] == 0:
	    #all_positions[posy][posx] = 1
	    #computer_move = True
    #else:
	#randomComputerAI(all_positions)

    #if computer_move == True:
         #drawComputer(posx, posy, 0)
         #return computer_move
