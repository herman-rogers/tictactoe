import pygame, sys, os, random
from pygame.locals import* #not sure if we will need this

#These top variables help get rid of magic numbers
#Variables to set screen and grid sizes

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOARDWIDTH = 3
BOARDHEIGHT = 3
BOXSIZE = 130

#Color Index -- Changing these values changes the colors
#          R   G   B
WHITE = ((255,255,255))
BLACK = ((0,0,0))
DARKTURQUOISE = ((3,54,73))
BRIGHTBLUE = ((0, 50, 255, 0))

BORDERCOLOR = BRIGHTBLUE
BACKCOLOR = DARKTURQUOISE
BOARDCOLOR = WHITE
TILECOLOR = BLACK#Possibly Delete This

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def mainGame():
        global FPSCLOCK, SURFACE
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        mousex = 0
        mousey = 0
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        gamestate = 1   

        mainBoard = generateNewBoard(80)


########This is the Main loop###########
        while gamestate == 1:
            for event in pygame.event.get():
            #    if event.type == MOUSEBUTTONUP:
            #        spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

            #    if (spotx, spoty) == (None, None):
            #        if RESET_RECT.collidepoint(event.pos) #This is for the Reset Button
            #   
            #    else:

            #        blankx, blanky = getBlankPosition(mainBoard)





                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gamestate = 0 

            pygame.display.flip()
            drawBoard(mainBoard)
        gameExit()


def gameExit():
    pygame.quit()
    exit()

def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * BOXSIZE) + (tileX - 1)
    top = YMARGIN + (tileY * BOXSIZE) + (tileY - 1)
    return (left, top)

def drawSquare(tilex, tiley, number, adjx = 0, adjy = 0):
    left, top = getLeftTopOfTile(tilex, tiley,) 
    pygame.draw.rect(SURFACE, TILECOLOR, (left + adjx, top + adjy, BOXSIZE, BOXSIZE))
 
def drawBoard(board): 
    SURFACE.fill(BACKCOLOR) 
    
    left, top = getLeftTopOfTile(0,0)
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

################## Starting Function ####################

if __name__ == '__main__':
    mainGame()
