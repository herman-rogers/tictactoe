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

    def testMouseCoords(self):
        self.assertTrue(self.get_board.mouseCoords())

    def testMovePositionRetunsValue(self):
        values_returned = [0,1,2,3,4,5,6,7,8,None]
        self.assertIn(self.get_board.movePosition(), values_returned)

    def testGetMouseClickReturnsTupleCoords(self):
        tuples_returned = [(None,None),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        self.assertIn(self.get_board.getMouseClick(), tuples_returned)

if __name__ == '__main__':
    unittest.main()
