import pygame, sys, os, random
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWWIDTH = 480

DARKTURQUOISE = ((3,54,73))

BACKCOLOR = DARKTURQUOISE



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

def mainMenu():

    global FPSCLOCK, SURFACE
    pygame.init()
    pygame.display.set_caption('Tic-Tac-Toe')
    FPSCLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    gamestate = 1
