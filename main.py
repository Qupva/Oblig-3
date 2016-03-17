#! /usr/env/bin python3

import pygame
import Vector2D
import LocalClient
import config as c

from player import *
from weapons import *


class game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_X, c.SCREEN_Y))

        self.player1 = player(self, 1, (c.GAME_SCALE * 2), (c.SCREEN_Y // 2))
        self.player2 = player(self, 2, (c.SCREEN_X - c.GAME_SCALE * 2), (c.SCREEN_Y // 2))

    def run(self):
        self.clock = pygame.time.Clock()
        
        while True:
            self.time_passed = self.clock.tick(60)
            self.time_passed_seconds = self.time_passed / 1000.0

            self.handle_event()
            self.handle_move()
            self.handle_draw()

    def handle_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def handle_move(self):
        self.player1.move()

    def handle_draw(self):
        self.screen.fill((40,32,40))

        self.player1.draw(self.screen)


        pygame.display.flip()



if __name__ == '__main__':
    spill = game()
    spill.run()