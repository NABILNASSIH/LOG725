
import pgzero, pgzrun
import pygame
from pygame.locals import *

#Component classes
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy

class Sprite:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.imageRect = self.image.get_rect()