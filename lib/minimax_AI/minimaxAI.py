from lib.loading_data.loadingdata import *

class AI(object):

    '''Class for determining both player and computer moves'''
    winning_moves = (
              [0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6],
                    )

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, all_positions=[]):
        if len(all_positions) == 0:
            self.all_positions = [0 for i in range(9)]

    def trackMovesLeft(self):
        return [k for k, v in enumerate(self.all_positions) if v is 0]

    def getPositions(self, player):
        return [k for k, v in enumerate(self.all_positions) if v == player]

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

board_data = AI()

class computerMove(object):

    def determine(self, board_data, player):
        a = -2
        choices = []
        make_coords = list(product(range(3), repeat=2 ))

        if len(board_data.trackMovesLeft()) == 9:
            posx, posy = make_coords[4]
	    load_data.drawComputer(posy, posx, 0)
            return 4

        for move in board_data.trackMovesLeft():
            board_data.makeMove(move, player)
            variable = board_data.miniMax(board_data, getEnemy(player), -2, 2)
            board_data.makeMove(move, 0)
            if variable > a:
                a = variable
                choices = [move]
            elif variable == a:
                choices.append(move)

        try:
            choose_move = random.choice(choices)
            posx,posy = make_coords[choose_move]
            load_data.drawComputer(posy, posx, 0)
            return choose_move
        except IndexError:
            pass

computer_move = computerMove()

def getEnemy(player):
    if player == 'X':
        return 'O'
    return 'X'

def gameExit():
    pygame.quit()
    exit()
