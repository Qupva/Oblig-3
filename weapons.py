""" Module contains weapon systems """

import pygame
import Vector2D
import config as c

from main import *
from player import *


class weapon(pygame.sprite.Sprite):
    """ Class that fires bullets """
    def fire(self, game, player):
        """ Metod that fires bullets and ads them to the bullet-list """

        self.bullet = bullet(player)
        game.bullet_list.add(self.bullet)


class bullet(pygame.sprite.Sprite):
    """ Bullet class """
    def __init__(self, player):
        super().__init__()
        
        tmp_img = pygame.image.load(c.BULLET_FNAME).convert_alpha()

        self.img = pygame.transform.scale(tmp_img, (c.BULLET_SIZE_X, c.BULLET_SIZE_Y))

        self.timer = c.BULLET_TIME
        self.rotation = player.rotation
        self.dir = Vector2D.Vector2D(0,0).convert(self.rotation)
        self.image = pygame.transform.rotate(self.img, self.rotation)

        self.pos = Vector2D.Vector2D(player.vel.x, player.vel.y)

        start_pos = Vector2D.Vector2D((player.rect.centerx), (player.rect.centery))

        start_pos.x += (player.height + c.GAME_SCALE) * self.dir.x
        start_pos.y += (player.height + c.GAME_SCALE) * self.dir.y

        self.rect = self.img.get_rect()
        self.rect = self.rect.move(start_pos.x, start_pos.y)

    def move(self, game):
        """ Handles how the bullet moves """

        self.timer -= game.time_passed_seconds
        self.pos += self.dir * c.BULLET_SPEED

        self.rect = self.rect.move(self.pos.x, self.pos.y)

        if self.timer <= 0:
            self.on_hit()
        
        if self.rect.x > (c.SCREEN_X + c.GAME_SCALE * 2) or self.rect.y > (c.SCREEN_Y + c.GAME_SCALE * 2):
            self.on_hit()
        elif self.rect.x < (0 - c.GAME_SCALE * 2) or self.rect.y < (0 - c.GAME_SCALE * 2):
            self.on_hit()


    def on_hit(self):
        """ Handles what happenes when bullet hits something """

        self.kill()