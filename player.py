
import pygame
import Vector2D
import config as c

from main import *
from weapons import *


class player(pygame.sprite.Sprite):
    def __init__(self, game, playernum, x, y):
        super().__init__()

        self.width = c.PLAYER_SIZE
        self.height = c.PLAYER_SIZE

        if playernum == 1:
            self.image = pygame.image.load(c.P1_FNAME).convert_alpha()

        elif playernum == 2:
            self.image = pygame.image.load(c.P2_FNAME).convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.pos = Vector2D.Vector2D(x, y)
        self.dir = Vector2D.Vector2D(0, -1).normalized()
        self.vel = Vector2D.Vector2D(0, 0)
        self.grav_dir = Vector2D.Vector2D(0, 1).normalized()

        self.rotation = 0

        
    def move(self):
        vector = Vector2D.Vector2D(0, 0)

        self.rotation = self.rotation % 360
        self.dir.convert(self.rotation)

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

        self.pos += vector

        self.pos.x = self.pos.x % c.SCREEN_X
        self.pos.y = self.pos.y % c.SCREEN_Y


    def draw(self, screen):
        img = pygame.transform.rotate(self.image, self.rotation)

        screen.blit(img, (self.pos.x, self.pos.y))
        #pygame.draw.line(screen, (0,240,0), (self.pos.x, self.pos.y), (self.pos.x + (self.dir.x * 10), self.pos.y + (self.dir.y * 10)), 3)