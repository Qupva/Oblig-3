
import pygame
import Vector2D
import config as c

from main import *
from player import *


class weapon(pygame.sprite.Sprite):
    def fire(self, game, player):
        self.bullet = bullet(player)
        game.bullet_list.add(self.bullet)


class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        
        tmp_img = pygame.image.load(c.BULLET_FNAME).convert_alpha()

        self.img = pygame.transform.scale(tmp_img, (c.BULLET_SIZE_X, c.BULLET_SIZE_Y))

        self.rotation = player.rotation
        self.dir = Vector2D.Vector2D(0,0).convert(self.rotation)
        self.image = pygame.transform.rotate(self.img, self.rotation)

        self.pos = Vector2D.Vector2D(player.pos.x, player.pos.y)

        start_pos = Vector2D.Vector2D((player.rect.x + player.width // 2), (player.rect.y + player.height // 2))

        start_pos.x += ((player.height / 2) + (player.height / 4)) * self.dir.x
        start_pos.y += ((player.height / 2) + (player.height / 4)) * self.dir.y

        self.rect = self.img.get_rect()
        self.rect = self.rect.move(start_pos.x, start_pos.y)

    def move(self, game):
        self.pos += self.dir * c.BULLET_SPEED

        self.rect = self.rect.move(self.pos.x, self.pos.y)

        if self.rect.x > (c.SCREEN_X + c.GAME_SCALE * 2) or self.rect.y > (c.SCREEN_Y + c.GAME_SCALE * 2):
            self.on_hit(game)
        elif self.rect.x < (0 - c.GAME_SCALE * 2) or self.rect.y < (0 - c.GAME_SCALE * 2):
            self.on_hit(game)

    def on_hit(self, game):
        game.bullet_list.remove(self)