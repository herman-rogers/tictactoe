import pygame, sys, os, random, time
from pygame.locals import*

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


#Tracking the Player, Computer, and Valid Moves

XMOVES = []
COMPUTERMOVES = []


XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def mainGame():
        global FPSCLOCK, SURFACE, RESET_RECT
        pygame.init()
        pygame.display.set_caption('Tic-Tac-Toe')
        turn = random.choice(['computer', 'player'])
        mousex = 0
        mousey = 0
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        gamestate = 1
        mainBoard = generateNewBoard(80) 
        VALIDMOVES = [1,2,3,4,5,6,7,8,9]
        xMoves = []
        oMoves = []

        winningMoves = (
            [1,4,7], [1,2,3], [1,5,9],
            [2,5,8], [3,5,7], [3,2,1])

########This is the Main loop###########
        while gamestate == 1:
            if turn == 'player':
                if VALIDMOVES == []:
                    gameExit()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        spotx, spoty = getMouseClick(mainBoard, event.pos[0], event.pos[1])
                        playerOnex, playerOney = getPlayerPosition(mainBoard)   
                     
                        if (spotx, spoty) == (playerOnex, playerOney) and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                            posx, posy = playerOnex, playerOney
                            drawCircle(posx, posy, 0,0)
                            turn = 'computer'
                
                        else:
                            #This finds players mouse position,
                            # anchors itself to board position 5, then adjusts according to mouse location

                            if (spotx, spoty) == (playerOnex + 1, playerOney) and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True:
                                posx, posy = playerOnex + 1, playerOney
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                            elif (spotx, spoty) == (playerOnex, playerOney + 1) and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                                posx, posy = playerOnex, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                            elif spotx == playerOnex and spoty == playerOney - 1 and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                                posx, posy = playerOnex, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                            elif spotx == playerOnex - 1 and spoty == playerOney and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                                posx, posy = playerOnex - 1, playerOney
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'
 
                            elif spotx == playerOnex - 1 and spoty == playerOney + 1 and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                                posx, posy = playerOnex - 1, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'
 
                            elif spotx == playerOnex + 1 and spoty == playerOney + 1 and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True: 
                                posx, posy = playerOnex + 1, playerOney + 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                            elif spotx == playerOnex - 1 and spoty == playerOney - 1 and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True:  
                                posx, posy = playerOnex - 1, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                            elif spotx == playerOnex + 1 and spoty == playerOney - 1 and getValidMoves(mainBoard, VALIDMOVES, oMoves) == True:
                                posx, posy = playerOnex + 1, playerOney - 1
                                drawCircle(posx, posy, 0,0)
                                turn = 'computer'

                if oMoves in winningMoves:
                    print 'Yay You Won'
                    gameExit()

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gamestate = 0

            elif turn == 'computer':

                if VALIDMOVES == []:
                    gameExit()

                ##A little function that will sleep the computer

                pauseUntil = time.time() + random.randint(2,5)*0.1
                while time.time() < pauseUntil:
                    pygame.display.update()

                if getComputerMove(mainBoard, VALIDMOVES, xMoves) == True:
                    turn = 'player'


            pygame.display.update()
        gameExit()

def gameExit():
    pygame.quit()
    exit()

##These Functions Draw the Player One Circle##

def getPlayerPosition(board):
    #Find the position
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == 5:
                return(x,y)

def getComputerMove(board, VALIDMOVES, xMoves):
    
    makeMove = False
    posx = random.randint(0,2)
    posy = random.randint(0,2)

    if makeMove == False:

        if (posx, posy) == (0,1) and 2 in VALIDMOVES:
            VALIDMOVES.remove(2)
            COMPUTERMOVES.append(2)

            makeMove = True


        elif (posx, posy) == (1,1) and 5 in VALIDMOVES:
            VALIDMOVES.remove(5)
            COMPUTERMOVES.append(5)

            makeMove = True

        elif (posx, posy) == (2,1) and 8 in VALIDMOVES:
            VALIDMOVES.remove(8)
            COMPUTERMOVES.append(8)

            makeMove = True

        ##Top Row Values [1,4,7]
        elif (posx, posy)== (0,0) and 1 in VALIDMOVES:
            VALIDMOVES.remove(1)
            COMPUTERMOVES.append(1)

            makeMove = True

        elif (posx, posy) == (1,0) and 4 in VALIDMOVES:
            VALIDMOVES.remove(4)
            COMPUTERMOVES.append(4)

            makeMove = True

        elif (posx, posy) == (2,0) and 7 in VALIDMOVES:
            VALIDMOVES.remove(7)
            COMPUTERMOVES.append(7)
            
            makeMove = True

    ##Bottom Row Values [3,6,9]
        elif (posx, posy) == (0,2) and 3 in VALIDMOVES:
            VALIDMOVES.remove(3)
            COMPUTERMOVES.append(3)
            makeMove = True

        elif (posx, posy)== (1,2) and 6 in VALIDMOVES:
            VALIDMOVES.remove(6)
            COMPUTERMOVES.append(6)

            makeMove = True

        elif (posx, posy) == (2,2) and 9 in VALIDMOVES:
            VALIDMOVES.remove(9)
            COMPUTERMOVES.append(9)

            makeMove = True

    else:
        return getComputerMove(board)

    if makeMove == True:
        drawX(posx, posy, 0)
        return makeMove

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

##This is the Computer AI functions and values checking for valid moves

def getValidMoves(board, VALIDMOVES, oMoves):

    isValid = True
    posx, posy = pygame.mouse.get_pos()
    i = getMouseClick(board, posx, posy)

    ##Center Row Values [2,5,8]
    if i == (0,1) and 2 in VALIDMOVES:
        VALIDMOVES.remove(2)
        oMoves.append(2)
        return isValid

    elif i == (1,1) and 5 in VALIDMOVES:
        VALIDMOVES.remove(5)
        oMoves.append(5)
        return isValid

    elif i == (2,1) and 8 in VALIDMOVES:
        VALIDMOVES.remove(8)
        oMoves.append(8)
        return isValid

    ##Top Row Values [1,4,7]
    elif i == (0,0) and 1 in VALIDMOVES:
        VALIDMOVES.remove(1)
        oMoves.append(1)
        return isValid

    elif i == (1,0) and 4 in VALIDMOVES:
        VALIDMOVES.remove(4)
        oMoves.append(4)
        return isValid

    elif i == (2,0) and 7 in VALIDMOVES:
        VALIDMOVES.remove(7)
        oMoves.append(7)
        return isValid

    ##Bottom Row Values [3,6,9]
    elif i == (0,2) and 3 in VALIDMOVES:
        VALIDMOVES.remove(3)
        oMoves.append(3)
        return isValid

    elif i == (1,2) and 6 in VALIDMOVES:
        VALIDMOVES.remove(6)
        oMoves.append(6)
        return isValid

    elif i == (2,2) and 9 in VALIDMOVES:
        VALIDMOVES.remove(9)
        oMoves.append(9)
        return isValid

    else:
        print ('Returned False')
        print oMoves
        isValid = False
        return isValid

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
