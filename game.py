import pygame, sys, os, random, time
from pygame.locals import*

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOARDWIDTH = 3
BOARDHEIGHT = 3
BOXSIZE = 130
CIRCLESIZE = 60
DONUTSIZE = 50
XSIZE = 80

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


def mainGame():
        global FPSCLOCK, SURFACE, RESET_RECT
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        turn = True
        mousex = 0
        mousey = 0
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        gamestate = 1
        mainBoard = generateNewBoard(80) 

########This is the Main loop###########
        while gamestate == 1:
            if turn == True:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        spotx, spoty = getMouseClick(mainBoard, event.pos[0], event.pos[1])
                        playerOnex, playerOney = getPlayerPosition(mainBoard)
 
                        if (spotx, spoty) == (playerOnex, playerOney): 
                            posx, posy = playerOnex, playerOney
                            drawCircle(posx, posy, 0,0)
                          #  turn = 'computer'
                
                        else:
                            #This finds players mouse position,
                            # anchors itself to board position 5, then adjusts according to mouse location
                        
                            if spotx == playerOnex + 1 and spoty == playerOney:
                                posx, posy = playerOnex + 1, playerOney
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'

                            elif spotx == playerOnex and spoty == playerOney + 1: 
                                posx, posy = playerOnex, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'

                            elif spotx == playerOnex and spoty == playerOney - 1: 
                                posx, posy = playerOnex, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'
 
                            elif spotx == playerOnex - 1 and spoty == playerOney: 
                                posx, posy = playerOnex - 1, playerOney
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'
 
                            elif spotx == playerOnex - 1 and spoty == playerOney + 1: 
                                posx, posy = playerOnex - 1, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'
 
                            elif spotx == playerOnex + 1 and spoty == playerOney + 1: 
                                posx, posy = playerOnex + 1, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'

                            elif spotx == playerOnex - 1 and spoty == playerOney - 1: 
                                posx, posy = playerOnex - 1, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'

                            elif spotx == playerOnex + 1 and spoty == playerOney - 1: 
                                posx, posy = playerOnex + 1, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                            #    turn = 'computer'

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gamestate = 0

            pygame.display.update()
        gameExit()

def gameExit():
    pygame.quit()
    exit()

def isValidMove(board):
    pass

##These Functions Draw the Player One Circle##

def getPlayerPosition(board):
    #Find the position
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == 5:
                return(x,y)

def drawCircle(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65 #to center circle divide BOXSIZE/2, then adjust both top and left
    pygame.draw.circle(SURFACE, CIRCLECOLOR, (centerleft + adjx, centertop + adjy), CIRCLESIZE)
    pygame.draw.circle(SURFACE, TILECOLOR, (centerleft + adjx, centertop + adjy), DONUTSIZE) #this is the inside of the Circle

def drawX(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley)
    centerleft, centertop = left + 65, top + 65


def drawSquare(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley,) 
    pygame.draw.rect(SURFACE, TILECOLOR, (left + adjx, top + adjy, BOXSIZE, BOXSIZE))

##Main Functions that Find Mouse Position and Top/Left Coords Relative to Tile Square##
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

##These Functions Draw the Main Board##

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
    #Returns Values for Board
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

##################STARTING FUNCTION###################

if __name__ == '__main__':
    mainGame()
