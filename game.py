import pygame, sys, os, random, time, itertools
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

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

def mainGame():
        global FPSCLOCK, SURFACE, RESET_RECT
        pygame.init()
        pygame.display.set_caption('Tic-Tac-War')
        turn = random.choice(['computer', 'player'])
        player1 = 1
        player2 = 2
        mousex = 0
        mousey = 0
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        game_state = 1
        mainBoard = generateNewBoard(80)
        all_positions = [ ##Board Data Structure
               [0,0,0],
	       [0,0,0],
	       [0,0,0],
	       ]
 
########This is the Main loop###########
        while game_state == 1:
            if turn == 'player':

                if noMoreMoves(all_positions) == False:
                    print 'This Game is a Draw'
                    gameExit()

                elif winningMoves(all_positions) == False:
                    print 'Computer Won the Game'
                    gameExit()

                for event in pygame.event.get():

                       if event.type == MOUSEBUTTONUP:

                           if movePosition(mainBoard, all_positions) == True:
                               turn = 'computer'

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gameExit()

            elif turn == 'computer':

                if noMoreMoves(all_positions) == False:
                    print 'This Game is a Draw'
                    gameExit()

                elif winningMoves(all_positions) == False:
                    print 'You Has Won, Sire'
                    gameExit()

                ##Make the computer seem like it's thinking

                pauseUntil = time.time() + random.randint(2,5)*0.1
                while time.time() < pauseUntil:
                    pygame.display.update()

                if getComputerMove(all_positions) == True:
                    turn = 'player'

            pygame.display.update()
        gameExit()

def gameExit():
    pygame.quit()
    exit()

def getComputerMove(all_positions):

    posx = random.randint(0,2)
    posy = random.randint(0,2)
    computer_move = False

    if computer_move == False:

        if (posx, posy) == (0,1) and all_positions[1][0] == 0:
            all_positions[1][0] = 2
            computer_move = True

        elif (posx, posy) == (1,1) and all_positions[1][1] == 0:
            all_positions[1][1] = 2
            computer_move = True


        elif (posx, posy) == (2,1) and all_positions[1][2] == 0:
            all_positions[1][2] = 2 
            computer_move = True


    ##Top Row Values [1,4,7]
        elif (posx, posy) == (0,0) and all_positions[0][0] == 0:
            all_positions[0][0] = 2
            computer_move = True

        elif (posx, posy) == (1,0) and all_positions[0][1] == 0:
            all_positions[0][1] = 2
            computer_move = True


        elif (posx, posy) == (2,0) and all_positions [0][2] == 0:
            all_positions[0][2] = 2
            computer_move = True


    ##Bottom Row Values [3,6,9]
        elif (posx, posy) == (0,2) and all_positions[2][0] == 0:
            all_positions[2][0] = 2
            computer_move = True


        elif (posx, posy)== (1,2) and all_positions[2][1] == 0:
            all_positions[2][1] = 2
            computer_move = True


        elif (posx, posy) == (2,2) and all_positions[2][2] == 0:
            all_positions[2][2] = 2
            computer_move = True

    else:
	getComputerMove(all_positions)

    if computer_move == True:
         drawX(posx, posy, 0)
         return computer_move




##This Registers the Player's Move

def movePosition(board, all_positions):

    posx, posy = pygame.mouse.get_pos()
    mousex, mousey = getMouseClick(board, posx, posy)

    ##Center Row Values [2,5,8]
    if (mousex, mousey) == (0,1) and all_positions[1][0] == 0:
        all_positions[1][0] = 1

    elif (mousex, mousey) == (1,1) and all_positions[1][1] == 0:
        all_positions[1][1] = 1

    elif (mousex, mousey) == (2,1) and all_positions[1][2] == 0:
        all_positions[1][2] = 1 

    ##Top Row Values [1,4,7]
    elif (mousex, mousey) == (0,0) and all_positions[0][0] == 0:
        all_positions[0][0] = 1
    
    elif (mousex, mousey) == (2,2) and all_positions[2][2] == 0:
        all_positions[2][2] = 1

    elif (mousex, mousey) == (1,0) and all_positions[0][1] == 0:
        all_positions[0][1] = 1

    elif (mousex, mousey) == (2,0) and all_positions [0][2] == 0:
        all_positions[0][2] = 1

    ##Bottom Row Values [3,6,9]
    elif (mousex, mousey) == (0,2) and all_positions[2][0] == 0:
        all_positions[2][0] = 1

    elif (mousex, mousey) == (1,2) and all_positions[2][1] == 0:
        all_positions[2][1] = 1

    elif (mousex, mousey) == (2,2) and all_positions[2][2] == 0:
        all_positions[2][2] = 1

    else:
       
        print 'Returning a False, Captain' 
        return False

    drawCircle(mousex, mousey,0,0)
    return True

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

def winningMoves(all_positions):

    print availableMoves(all_positions)
    
    numberRows = len(all_positions)
    lft = [ [0] * i for i in range(numberRows) ]
    reverselist = list(reversed(lft))

    transpositions = {
    'horizontal' : all_positions,
    'vertical'    : zip(*all_positions),
    'diag_forw'  : zip(* [lft[i] + all_positions[i] + reverselist[i] for i in range(numberRows)] ),
    'diag_back'  : zip(* [reverselist[i] + all_positions[i] + lft[i] for i in range(numberRows)] ),
    }

    for direction, transp in transpositions.iteritems():
        for row in transp:
            string = ''.join(map(str, row))
            for player in range(1,3):
                if string.find(str(player) * 3) >= 0:
                    print 'player={0} direction={1}'.format(player, direction)
                    return False
    return True

def noMoreMoves(all_positions):

    no_moves_left = itertools.chain.from_iterable(all_positions)
    if 0 not in no_moves_left:
        return False
    return True

#############Constructing the minimax formula#######################################################




def availableMoves(all_positions):

    make_list = itertools.chain.from_iterable(all_positions)
    return [k for k, v in enumerate(make_list) if v is 0]


def getUtility(node, all_positions):




############################################END OF CONSTRUCTION#######################################


## Drawing the Main Game Board

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



## Images and Image Handling

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
