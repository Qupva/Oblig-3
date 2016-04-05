
import pygame
import Vector2D
import config as c

from main import *
from weapons import *


class player1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()

        self.width = c.PLAYER_SIZE
        self.height = c.PLAYER_SIZE

        self.image = pygame.image.load(c.P1_FNAME).convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.pos = Vector2D.Vector2D(x, y)
        self.dir = Vector2D.Vector2D(0, -1).normalized()
        self.vel = Vector2D.Vector2D(0, 0)
        self.grav_dir = Vector2D.Vector2D(0, 1).normalized()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos.x, self.pos.y)

        self.rotation = 0

        
    def move(self):
        vector = Vector2D.Vector2D(0, 0)

        self.rotation = self.rotation % 360
        self.dir = self.dir.convert(self.rotation)

        self.vel += self.grav_dir * c.GRAVITY

        if self.vel.magnitude() <= 0:
            self.vel.x = 0
            self.vel.y = 0
        else:
            self.vel.x -= self.vel.x / c.AIR_RESISTANCE
            self.vel.y -= self.vel.y / c.AIR_RESISTANCE

        vector = self.vel

        if vector.magnitude() > c.MAX_SPEED:
            vector = vector.normalized() * c.MAX_SPEED

        self.pos = vector

        self.rect = self.rect.move(self.pos.x, self.pos.y)

        self.rect.x = self.rect.x % c.SCREEN_X
        self.rect.y = self.rect.y % c.SCREEN_Y

"""
    def draw(self, screen):
        img = pygame.transform.rotate(self.image, self.rotation)

        screen.blit(img, (self.pos.x, self.pos.y))
"""

class player2(player1):
    def __init__(self, game, x, y):

        super().__init__(game, x, y)

        self.image = pygame.image.load(c.P2_FNAME).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))