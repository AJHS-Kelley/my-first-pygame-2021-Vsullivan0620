# My First PyGame, Victor Sullivan, 11/30/2021, 2:14 PM, v0.0

import pygame, sys
from pygame.locals import *

#Start PyGame
pygame.init()

# Setup the game window.
windowSurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption('Hello, world!')

#Setup Color values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGNETBLUE = (52, 186, 235)

#Setup fonts.
basicFont = pygame.font.SysFont(None, 48)

#Setup text. 
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
