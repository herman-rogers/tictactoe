import pygame, os, sys, random, time, pygame.mixer
from pygame.locals import *
from itertools import *

class windowSet(object):

    clock = pygame.time.Clock()
    window_width, window_height = 1280, 720 #854, 480
    surface = pygame.display.set_mode((window_width, window_height))

    board_width, board_height = 3,3
    box_size, x_size = 130,130

    x_margin = int((window_width - (box_size * board_width + (board_width - 1))) / 2)
    y_margin = int((window_height - (box_size * board_height + (board_height - 1))) / 2)

    def getLeftTopCoords(self, tileX, tileY):
        left = self.x_margin + (tileX * self.box_size) + (tileX - 1)
        top = self.y_margin + (tileY * self.box_size) + (tileY - 1)
        return (left, top) 

window_set = windowSet()


