
import pygame
import Vector2D
import config as c

from main import *
from player import *


class weapon(pygame.sprite.Sprite):
    def fire(self, game, player):
        print("fire!")
        self.bullet = bullet(player)
        game.bullet_list.add(self.bullet)


class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        
        tmp_img = pygame.image.load(c.BULLET_FNAME).convert_alpha()

        self.img = pygame.transform.scale(tmp_img, (c.BULLET_SIZE_X, c.BULLET_SIZE_Y))

        self.pos = Vector2D.Vector2D(player.pos.x, player.pos.y)
        self.vel = Vector2D.Vector2D(0, 0)
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(self.pos.x, self.pos.y)

        self.dir = player.dir
        self.rotation = player.rotation
        self.image = pygame.transform.rotate(self.img, self.rotation)

    def move(self):
        self.vel.x = c.BULLET_SPEED * self.dir.x
        self.vel.y = c.BULLET_SPEED * self.dir.y

        self.pos += self.vel

        self.rect = self.rect.move(self.pos.x, self.pos.y)

    def on_hit(self):
        pass