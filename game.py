import pygame, sys, os, random, time, itertools, operator
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
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        
        turn = random.choice(['computer', 'player'])
     #   winner = ('X-win', 'Draw', 'O-win')
        mousex, mousey = 0,0
        game_state = 1
        mainBoard = generateNewBoard(80)
        all_positions = [     ##Board Data Structure##
               [0,0,0],
	       [0,0,0],
	       [0,0,0],
	       ]
 
########This is the Main loop###########
        while game_state == 1:
            if turn == 'player':
                if winningMoves(all_positions) == True:
                    gameExit()

                for event in pygame.event.get():
                       if event.type == MOUSEBUTTONUP:

                           if movePosition(mainBoard, all_positions) == True:
                               turn = 'computer'

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    
                    gameExit()

            elif turn == 'computer':
                if winningMoves(all_positions) == True:
                    print 'You Has Won, Sire'
                    gameExit()

                ##Make the computer seem like it's thinking

                pauseUntil = time.time() + random.randint(2,5)*0.1
                while time.time() < pauseUntil:
                    pygame.display.update()

		if getComputerMove(mainBoard, all_positions) == True:
		    turn = 'player'

                #if determine(all_positions) == True:
                    #turn = 'player'
                     

            pygame.display.update()
        gameExit()

def gameExit():
    pygame.quit()
    exit()

def getComputerMove(board, all_positions):

    posx, posy = random.randint(0,2), random.randint(0,2)
    computer_move = False
    
    if computer_move == False:

	if all_positions[posy][posx] == 0:
	    all_positions[posy][posx] = 2
	    computer_move = True
    else:
	getComputerMove(all_positions)

    if computer_move == True:
         drawX(posx, posy, 0)
         return computer_move

def movePosition(board, all_positions):

##The values from the coordinates are inverses of the board coordinates. Therefore, we can call the
##mouse coordinates x y and pass them into all_positions nested list as y x to get correct positioning.

    posx, posy = pygame.mouse.get_pos()
    mousex, mousey = getMouseClick(board, posx, posy)

    if all_positions[mousey][mousex] == 0:
        all_positions[mousey][mousex] = 1
        drawCircle(mousex, mousey, 0,0)
        return True

    print 'Returning a False, Captain' 
    return False

def winningMoves(all_positions):

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
                    print 'player={0} direction={1}'.format(player, direction)    ##Uncomment to check player/position debugging
                    return True
    return False

def trackMovesLeft(all_positions):

    list_of_moves = itertools.chain.from_iterable(all_positions)
    moves_left = [k for k, v in enumerate(list_of_moves) if v is 0]
    return moves_left   

#############Constructing the minimax algo#######################################################

def makeMove(all_positions, position):
   all_positions[position] = player

def minimax(node, player):
    if node.winningMoves(all_positions):
        if node.player == 1:
            return -1
        if node.player == 0:
            return 0
        elif node.player == 2:
            return 1

    best = None
   
    for move in node.availableMoves(all_positions):
	make_move(move, player)
	val = minimax(node, enemy, alpha, beta)
	node.make_move(move, None)
	if player == 2:
	    if val > best:
		best = val
	else:
	    if val < best:
		best = val
	return best

#def determine(all_positions):
    #a = -2
    #choices = []

    #for move in availableMoves(all_positions):
	#availableMoves.make_move(move, player)
	#val = board.minimax(all_positions, player, -2, 2)
	#board.make_move(move, None)

	#if val > a:
	    #a = val
	    #choices = [move]
	#elif val == a:
	    #choices.append(move)
    #return random.choice(choices)

#def availableMoves(all_positions):
    #make_list = itertools.chain.from_iterable(all_positions)
    #return [k for k, v in enumerate(make_list) if v is None]

def computerMinimax(all_positions):

    if len(trackMovesLeft(all_positions)) == 9:
        all_positions[1][1] = 1







#def itemInList(all_positions):

    #for inner_l in all_positions:
	#for item in inner_l:
	    #return item

#def make_move(position, player):
   #all_positions[position] = player 
 








############################################END OF CONSTRUCTION#######################################

##Coordinates for Board and Mouse Clicks
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
