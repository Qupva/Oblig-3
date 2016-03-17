
import pygame
import Vector2D

from main import *
from config import *
from weapons import *


class player(pygame.sprite.Sprite):
    def __init__(self, game, playernum, x, y):
        super().__init__()

        self.width = GAME_SCALE * 5
        self.height = GAME_SCALE * 5

        if playernum == 1:
            self.image = pygame.image.load(P1_FNAME).convert_alpha()
            self.left = P1_L
            self.right = P1_R
            self.shoot = P1_S
            self.drive = P1_D

        elif playernum == 2:
            self.image = pygame.image.load(P2_FNAME).convert_alpha()
            self.left = P2_L
            self.right = P2_R
            self.shoot = P2_S
            self.drive = P2_D


        self.pos = Vector2D.Vector2D(x, y)
        self.dir = Vector2D.Vector2D(0, -1)
        self.vel = Vector2D.Vector2D(0, 0)

    def move(self):
        pass

    def move(self, screen):
        pass