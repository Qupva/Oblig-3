
import pygame
import Vector2D
import config as c

from main import *
from weapons import *

class asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        tmp_img = pygame.image.load(c.ASTEROID_FNAME).convert()
        self.image = pygame.transform.scale(tmp_img, (width, height))

        self.rect = pygame.Rect(x, y, width, height)


class platform(asteroid):
    def __init__(self, game, x, y):
        self.width = c.GAME_SCALE * 4
        self.height = c.GAME_SCALE * 1

        super().__init__(x, y, self.width, self.height)