
import pygame
import Vector2D
import config as c

from main import *
from weapons import *

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.wdith = c.GAME_SCALE * 2
        self.height = c.GAME_SCALE * 5

        tmp_img = pygame.image.load(c.ASTEROID_FNAME).convert()
        self.image = pygame.transform.scale(tmp_img, (self.wdith, self.height))

        self.rect = pygame.Rect(c.SCREEN_X // 2, c.SCREEN_Y // 2, self.wdith, self.height)