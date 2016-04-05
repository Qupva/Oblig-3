
import pygame
from main import *

P1_FNAME = "img/p1.png"
P2_FNAME = "img/p2.png"
BULLET_FNAME = "img/bullet.png"
HEART_FNAME = "ing/heart.png"
P1_TXT = "img/player_1_text.png"
P2_TXT = "img/player_2_text.png"

SCREEN_X, SCREEN_Y = 1200, 720
BG_COLOR = 40,32,40
GAME_SCALE = SCREEN_X // 100

GRAVITY = 0.5
MOVE_SPEED = 1.5
TURN_SPEED = 2.5
MAX_SPEED = 15
AIR_RESISTANCE = 10

FIRE_RATE = 0.2 # delay (in secounds) between shots
BULLET_SPEED = 1
BULLET_TIME = 1.0

PLAYER_SIZE = GAME_SCALE * 4
BULLET_SIZE_X = GAME_SCALE // 2
BULLET_SIZE_Y = BULLET_SIZE_X * 3

TIME_TOGGLE = pygame.K_SPACE

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

