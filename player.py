""" Module contains players and player logic """
import pygame
import Vector2D
import config as c

from main import *
from weapons import *


class player(pygame.sprite.Sprite):
    """ Player class gives player objects life, but no image """
    def __init__(self, game, x, y):
        super().__init__()

        self.width = c.PLAYER_SIZE
        self.height = c.PLAYER_SIZE

        self.img = pygame.transform.scale(self.tmp_img, (self.width, self.height))

        self.dir = Vector2D.Vector2D(0, -1).normalized()
        self.vel = Vector2D.Vector2D(0, 0)
        self.grav_dir = Vector2D.Vector2D(0, 1).normalized()
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(x, y)

        self.bullet_timer = c.FIRE_RATE

        self.weapon = weapon()

        self.rotation = 0

        self.score = 0
        self.fuel = c.MAX_FUEL

        
    def move(self, game):
        """ Handles player movement """

        self.rotation = self.rotation % 360
        self.dir = self.dir.convert(self.rotation)

        self.vel += self.grav_dir * c.GRAVITY * game.time_passed_seconds

        
        self.vel.x -= self.vel.x / c.AIR_RESISTANCE
        self.vel.y -= self.vel.y / c.AIR_RESISTANCE

        if self.vel.magnitude() > c.MAX_SPEED:
            self.vel = self.vel.normalized() * c.MAX_SPEED

        self.rect = self.rect.move(self.vel.x, self.vel.y)

        if self.rect.y + self.rect.height > c.SCREEN_Y:
            self.vel = self.vel * -1
            self.rect = self.rect.move(0, -1)

        if self.rect.x < 0:
            self.vel = self.vel * -1
            self.rect = self.rect.move(1, 0)
        elif self.rect.x + self.rect.width > c.SCREEN_X:
            self.vel = self.vel * -1
            self.rect = self.rect.move(-1, 0)

        self.image = pygame.transform.rotate(self.img, self.rotation)
        self.rect = self.image.get_rect(center = self.rect.center)


class player1(player):
    """ Gives player 1 a different image from other players """
    def __init__(self, game, x, y):

        self.tmp_img = pygame.image.load(c.P1_FNAME).convert_alpha()
        super().__init__(game, x, y)


class player2(player):
    """ Gives player 2 a different image from other players """
    def __init__(self, game, x, y):

        self.tmp_img = pygame.image.load(c.P2_FNAME).convert_alpha()
        super().__init__(game, x, y)