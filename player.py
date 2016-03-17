
import pygame
import Vector2D
import config as c

from main import *
from weapons import *


class player(pygame.sprite.Sprite):
    def __init__(self, game, playernum, x, y):
        super().__init__()

        self.width = c.GAME_SCALE * 5
        self.height = c.GAME_SCALE * 5

        if playernum == 1:
            self.image = pygame.image.load(c.P1_FNAME).convert_alpha()
            self.left = c.P1_L
            self.right = c.P1_R
            self.shoot = c.P1_S
            self.drive = c.P1_D

        elif playernum == 2:
            self.image = pygame.image.load(c.P2_FNAME).convert_alpha()
            self.left = c.P2_L
            self.right = c.P2_R
            self.shoot = c.P2_S
            self.drive = c.P2_D

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.pos = Vector2D.Vector2D(x, y)
        self.dir = Vector2D.Vector2D(0, -1).normalized()
        self.vel = Vector2D.Vector2D(0, 0)

        self.rotation = 0

        

    def move(self):
        self.rotation += 1

    def draw(self, screen):
        img = pygame.transform.rotate(self.image, self.rotation)

        screen.blit(img, (self.pos.x, self.pos.y))