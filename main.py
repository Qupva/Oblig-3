#! /usr/env/bin python3

import pygame
import Vector2D
import LocalClient

from config import *
from player import *
from weapons import *


class game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

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
        pass

    def handle_draw(self):
        self.screen.fill((32,32,40))


        pygame.display.flip()



if __name__ == '__main__':
    spill = game()
    spill.run()