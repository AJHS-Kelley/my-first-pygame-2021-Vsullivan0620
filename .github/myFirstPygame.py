# My First PyGame, Victor Sullivan, 11/30/2021, 2:14 PM, v0.0

import pygame, sys
from pygame.locals import *

#Start PyGame
pygame.init()

# Setup the game window.
windowSurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption('Hello, world!')