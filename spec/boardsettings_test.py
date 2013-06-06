import unittest, sys, os

sys.path.append("..")

from game import *

class testGraphicalSettingsStructure(unittest.TestCase):

    def setUp(self):
        self.get_board = createGraphicalBoard()
    
    def testGetBeginningGraphicalBoard(self):
        test_structure = [[1,4,7],[2,5,8],[3,6,9]]
        self.assertEqual(test_structure, self.get_board.getStartBoard())

    def testGenerateNewBoard(self):
        test_new_board = [[1,4,7],[2,5,8],[3,6,9]]
        board = self.get_board.getStartBoard()
        self.assertEqual(test_new_board, self.get_board.generateNewBoard(board))

if __name__ == '__main__':
    unittest.main()
