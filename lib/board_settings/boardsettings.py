from lib.window_settings.windowsettings import *
from lib.loading_data.loadingdata import *

class createGraphicalBoard(object):

    def movePosition(self, board, board_data, player):
        '''Get Board X,Y Coordinates from player and return list move'''
        posx, posy = pygame.mouse.get_pos()
        mousex, mousey = self.getMouseClick(board, posx, posy)
        get_list = zip(*[iter(enumerate(board_data.all_positions))]*3)
        get_matrix = map(list, zip(*get_list))

        try:
            for value in get_matrix[mousex][mousey]:
                if value in board_data.trackMovesLeft():
                    load_data.drawPlayer(mousex, mousey, 0,0)
                return value
        except TypeError:
            pass

    def getMouseClick(self, board, x, y):
        '''Converts mouse coordinates to board coordinates'''
        for tileX in range(len(board)):
            for tileY in range(len(board[0])):
                left, top = window_set.getLeftTopCoords(tileX, tileY)
                tileRect = pygame.Rect(left, top, window_set.box_size, window_set.box_size)
            
                if tileRect.collidepoint(x,y):
                    return(tileX, tileY)
        return (None,None)

    def drawBoard(self, board):
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

    def getStartBoard(self):
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

    def generateNewBoard(self, board):
        board = self.getStartBoard()
        self.drawBoard(board)
        pygame.display.update()
        return (board)

graphical_board = createGraphicalBoard()
