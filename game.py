import pygame, sys, os, random
from pygame.locals import* #not sure if we will need this

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOARDWIDTH = 3
BOARDHEIGHT = 3
BOXSIZE = 130
CIRCLESIZE = 100
SQUARESIZE = 100

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


XSHAPE = 'xshape'
CIRCLE = 'circle'

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def load_png(name):
    """This is so we can load objects relative paths"""
    fullname = os.path.join('/data', name)
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
        mousex = 0
        mousey = 0
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        gamestate = 1
        mainBoard = generateNewBoard(80)
        penguine_image = ("penguine.png") 

########This is the Main loop###########
        while gamestate == 1:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getMouseClick(mainBoard, event.pos[0], event.pos[1])


                if event.type == MOUSEBUTTONDOWN:
                    drawBoard(mainBoard)
                    playerCircle() 
               #     if (spotx, spoty) == (None, None):
               #         if RESET_RECT.collidepoint(event.pos):
               #             drawBoard(mainBoard)
               #             allMoves = [] 
               #     else:

               #         blankx, blanky = getBlankCoords(mainBoard)
 
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gamestate = 0 

            pygame.display.update()
        gameExit()

def playerCircle():
    mousex, mousey = 200, 200
    pygame.draw.circle(SURFACE, CIRCLECOLOR, (mousex, mousey), 50)


def gameExit():
    pygame.quit()
    exit()

def getBlankCoords(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == None:
                return(x,y)

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

def drawSquare(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopCoords(tilex, tiley,) 
    pygame.draw.rect(SURFACE, TILECOLOR, (left + adjx, top + adjy, BOXSIZE, BOXSIZE))
 
##CURRENT FUNCTION WORKING ON
 
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

#Drawing GameShapes

#def drawCircleAtPixel(shape, color, tileX, tileY):
#    for tilex in range(BOARDWIDTH):
#        for tileY in range(BOARDHEIGHT):
#            left, top = getLeftTopCoords(tileX,tileY)
#            playerCircle = pygame.Circle(left, top, CIRCLESIZE, CIRCLESIZE)
#            if boxCircle.collidepoint(x,y):
#                return(tileX, tileY)
#    return(None, None)
#
#
#def drawShapes(color, tileX, tileY):
#    quarter = int(BOXSIZE * 0.25)
#    half = int(BOXSIZE * 0.5)
#
#    left, top = getLeftTopCoords(tileX, tileY)
#
#    if shape == CIRCLE:
#    pygame.draw.circle(SURFACE, CIRCLECOLOR, (left + half, top + half), half - 5)
#    pygame.draw.circle(SURFACE, BOARDCOLOR, (left + half, top + half), quarter - 5)
#    elif shape == SQUARE:
#        pygame.draw.rect(SURFACE, CIRCLECOLOR, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))



##################STARTING FUNCTION###################

if __name__ == '__main__':
    mainGame()
