import unittest, sys, os

sys.path.append("..")

from game import *

class testGraphicalSettingsStructure(unittest.TestCase):

    def setUp(self):
        self.get_board = createGraphicalBoard()
        self.board = self.get_board.getStartBoard()
        self.test_structure = [[1,4,7],[2,5,8],[3,6,9]]

    def testGetBeginningGraphicalBoard(self):
        self.assertEqual(self.test_structure, self.board)

    def testGenerateNewBoard(self):
        self.assertEqual(self.test_structure, self.get_board.generateNewBoard(self.board))

#    def testReturnBoardCoordsOnMouseClick(self):
	#self.assertEqual(graphical_board.mouseCoords(), self.get_board.getMouseClick())

    #def testReturnNothinIfMouseIsOutsideBoard(self):
        #self.assertEqual((None,None), self.get_board.getMouseClick())

    #def testMouseCoordsReturn(self):
        #self.assertEqual(pygame.mouse.get_pos(), self.get_board.mouseCoords())

    #def testPlayerMovePosition(self):
        #posx, posy = 4,4
        #self.get_board.getMouseClick()
        #self.assertNotEqual(None, self.get_board.movePosition())

if __name__ == '__main__':
    unittest.main()
