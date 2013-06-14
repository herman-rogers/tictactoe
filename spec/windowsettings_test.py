import unittest, sys, os

sys.path.append("..")

from lib.window_settings.windowsettings import *
from lib.board_settings.boardsettings import *

class testWindowSettings(unittest.TestCase):

    def setUp(self):
        self.setting = window_set
        self.board = graphical_board

    def testBoardWidthAndHeightEqual(self):
        self.assertEqual(self.setting.board_width, self.setting.board_height)

    def testBoxSizeAndXSizeEqual(self):
        self.assertEqual(self.setting.x_size, self.setting.box_size)

    def testXMarginReturnsCorrectValue(self):
        self.assertEqual(self.setting.x_margin, 444)

    def testYMarginReturnsCorrectValue(self):
        self.assertEqual(self.setting.y_margin, 164)

    def testLeftTopCoordsValues(self):
        position = 443,163
        self.assertEqual(self.setting.getLeftTopCoords(0,0), position)

if __name__ == "__main__":
    unittest.main()
