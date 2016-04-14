
import pygame
import Vector2D
import config as c

from main import *
from weapons import *


class player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()

        self.width = c.PLAYER_SIZE
        self.height = c.PLAYER_SIZE

        self.img = pygame.transform.scale(self.tmp_img, (self.width, self.height))

        self.pos = Vector2D.Vector2D(x, y)
        self.dir = Vector2D.Vector2D(0, -1).normalized()
        self.vel = Vector2D.Vector2D(0, 0)
        self.grav_dir = Vector2D.Vector2D(0, 1).normalized()
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(self.pos.x, self.pos.y)

        self.bullet_timer = c.FIRE_RATE

        self.weapon = weapon()

        self.rotation = 0

        self.score = 0
        self.fuel = c.MAX_FUEL

        
    def move(self, game):
        vector = Vector2D.Vector2D(0, 0)

        self.rotation = self.rotation % 360
        self.dir = self.dir.convert(self.rotation)

        self.vel += self.grav_dir * c.GRAVITY * game.time_passed_seconds

        
        self.vel.x -= self.vel.x / c.AIR_RESISTANCE
        self.vel.y -= self.vel.y / c.AIR_RESISTANCE

        vector = self.vel

        if vector.magnitude() > c.MAX_SPEED:
            vector = vector.normalized() * c.MAX_SPEED

        self.pos = vector

        self.rect = self.rect.move(self.pos.x, self.pos.y)

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
    def __init__(self, game, x, y):

        self.tmp_img = pygame.image.load(c.P1_FNAME).convert_alpha()
        super().__init__(game, x, y)


class player2(player):
    def __init__(self, game, x, y):

        self.tmp_img = pygame.image.load(c.P2_FNAME).convert_alpha()
        super().__init__(game, x, y)