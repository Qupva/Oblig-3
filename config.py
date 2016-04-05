
import pygame
from main import *

P1_FNAME = "img/p1.png"
P2_FNAME = "img/p2.png"
BULLET_FNAME = "img/bullet.png"

SCREEN_X, SCREEN_Y = 1200, 720
GAME_SCALE = SCREEN_X // 100

GRAVITY = 0.9
MOVE_SPEED = 2
TURN_SPEED = 3
MAX_SPEED = 20
AIR_RESISTANCE = 50

FIRE_RATE = 0.5 # delay (in secounds) between shots
BULLET_SPEED = 1

PLAYER_SIZE = GAME_SCALE * 4
BULLET_SIZE_X = GAME_SCALE // 2
BULLET_SIZE_Y = BULLET_SIZE_X * 3

""" Image and keybinds for player 1 """
# Key to turn player left
P1_L = pygame.K_a

# Key to turn player right
P1_R = pygame.K_d

# Key to make the player move forward (drive)
P1_D = pygame.K_w

# Key to make the player fire it's weapon
P1_S = pygame.K_f

""" Image and keybinds for player 2 """
# Key to turn player left
P2_L = pygame.K_LEFT

# Key to turn player right
P2_R = pygame.K_RIGHT

# Key to make the player move forward (drive)
P2_D = pygame.K_UP

# Key to make the player fire it's weapon
P2_S = pygame.K_m

