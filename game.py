import pygame, sys, os, random, time, itertools, operator
from pygame.locals import*
from itertools import*

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
BOARDWIDTH = 3
BOARDHEIGHT = 3
BOXSIZE = 130
CIRCLESIZE = 60
INSIDECIRCLE = 50
XSIZE = 130
 
#Color Index -- Changing these values changes the colors
#          R   G   B
WHITE = ((255,255,255))
BLACK = ((0,0,0))
DARKTURQUOISE = ((3,54,73))
BRIGHTBLUE = ((0, 50, 255, 0))

BORDERCOLOR = BRIGHTBLUE
BACKCOLOR = DARKTURQUOISE
BOARDCOLOR = WHITE
TILECOLOR = BLACK
CIRCLECOLOR = WHITE
XCOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def mainGame():
        global FPSCLOCK, SURFACE, RESET_RECT
        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        turn = random.choice(['computer', 'player'])
        board_data = AI()
        mainBoard = generateNewBoard(80)
        gamestate = 1

        while not board_data.boardComplete():
            player = 'X'

            if turn == 'player':
#                if winningMoves(all_positions, player) == True:
                    #gameExit()

                for event in pygame.event.get():
                       if event.type == MOUSEBUTTONUP:

                           player_move = movePosition(mainBoard, board_data, player)
                           if not player_move in board_data.trackMovesLeft():
                               continue
                           board_data.makeMove(player_move, player)
                           turn = 'computer'

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gameExit()

            elif turn == 'computer':
#                if winningMoves(all_positions, player) == True:
                    #print 'You Has Won, Sire'
                    #gameExit()

                ##Make the computer seem like it's thinking
                pauseUntil = time.time() + random.randint(2,5)*0.1
                while time.time() < pauseUntil:
                    pygame.display.update()

       #         if randomComputerAI(all_positions) == True:
		    #turn = 'player'
                player = getEnemy(player)
		computer_move = determine(board_data, player)
		board_data.makeMove(computer_move, player)
                turn = 'player'
	    pygame.display.update()
        gameExit()

####NEXT AI ATTEMPT ####
class AI(object):

    winning_moves = (
              [0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6],
                    )

    winners = ('X-win', 'Draw', 'O-win')

    ##Board Data Structure !(Different from Graphical Data Structure)##
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
        self.all_positions[position] = player

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
#        print outcomes
        #print all_positions

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
	drawX(posy, posx, 0)
        return 4

    for move in board_data.trackMovesLeft():

        board_data.makeMove(move, player)
        variable = board_data.miniMax(board_data, getEnemy(player), -2, 2)
        board_data.makeMove(move, 0)
        print 'move:', move + 1, 'causes:', board_data.winners[variable]
        if variable > a:
            a = variable
            choices = [move]
        elif variable == a:
            choices.append(move)

    choose_move = random.choice(choices)
    posx,posy = make_coords[choose_move]
    drawX(posy, posx, 0)
    return choose_move

def getEnemy(player):
    if player == 'X':
        return 'O'
    return 'X'


def gameExit():
    pygame.quit()
    exit()

def movePosition(board, board_data, player):

##The values from the coordinates are inverses of the board coordinates. Therefore, we can call the
##mouse coordinates x y and pass them into all_positions nested list as y x to get correct positioning.
##We can do the same for the Easy computer AI.

    posx, posy = pygame.mouse.get_pos()
    mousex, mousey = getMouseClick(board, posx, posy)
    get_list = zip(*[iter(enumerate(board_data.all_positions))]*3)
    get_matrix = map(list, zip(*get_list))

    try:
        for value in get_matrix[mousex][mousey]:
            if value in board_data.trackMovesLeft():
                drawCircle(mousex, mousey, 0,0)
            return value
    except TypeError:
        pass
    print 'Returning a False, Captain' 

def randomComputerAI(all_positions):

    posx, posy = random.randint(0,2), random.randint(0,2)
    computer_move = False
 
    if computer_move == False:
	if all_positions[posy][posx] == 0:
	    all_positions[posy][posx] = 1
	    computer_move = True
    else:
	randomComputerAI(all_positions)

    if computer_move == True:
         drawX(posx, posy, 0)
         return computer_move

#### Coordinates for Board and Mouse Clicks
def getMouseClick(board, x, y):

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

#### Drawing the Main Game Board
def drawBoard(board): 

    SURFACE.fill(BACKCOLOR)     
    left, top = getLeftTopCoords(0,0)
    width = BOARDWIDTH * BOXSIZE
    height = BOARDHEIGHT * BOXSIZE
    pygame.draw.rect(SURFACE, BOARDCOLOR, (left - 5, top - 5, width + 11, height + 11)) 

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

#### Images and Image Handling

def drawCircle(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65 #to center circle divide BOXSIZE/2, then adjust both top and left
    pygame.draw.circle(SURFACE, CIRCLECOLOR, (centerleft + adjx, centertop + adjy), CIRCLESIZE)
    pygame.draw.circle(SURFACE, TILECOLOR, (centerleft + adjx, centertop + adjy), INSIDECIRCLE) #this is the inside of the Circle

def drawX(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65
 
    penguine_image = load_png("penguine.png")
    resizePenguine = pygame.transform.scale(penguine_image, (XSIZE, XSIZE))
    SURFACE.blit(resizePenguine, (left + adjx, top + adjy))

def drawSquare(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley,) 
    pygame.draw.rect(SURFACE, TILECOLOR, (left + adjx, top + adjy, BOXSIZE, BOXSIZE))

def load_png(name):
    """This is so we can load objects relative paths"""

    fullname = os.path.join('data/images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.conver_alpha()
    except pygame.error, message:
        print 'Seems like I lost your image:', fullname
        raise SystemExit, message
    return image



##################STARTING FUNCTION###################

if __name__ == '__main__':
    mainGame()

