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

        self.player_list = pygame.sprite.Group()

        self.player1 = player(self, 1, (c.GAME_SCALE * 2), (c.SCREEN_Y // 2))
        self.player2 = player(self, 2, (c.SCREEN_X - c.GAME_SCALE * 5), (c.SCREEN_Y // 2))

        self.player_list.add(self.player1)
        self.player_list.add(self.player2)

    def run(self):
        self.clock = pygame.time.Clock()
        
        while True:
            self.time_passed = self.clock.tick(60)
            self.time_passed_seconds = self.time_passed / 1000.0

            self.player_input()

            self.handle_event()
            self.handle_move()
            self.handle_draw()

    def player_input(self):
    
        """ Player 1 input """
        if pygame.key.get_pressed()[c.P1_L]:
            self.player1.rotation += c.TURN_SPEED

        if pygame.key.get_pressed()[c.P1_R]:
            self.player1.rotation -= c.TURN_SPEED

        if pygame.key.get_pressed()[c.P1_D]:
            self.player1.vel.x += self.player1.dir.x * c.MOVE_SPEED
            self.player1.vel.y += self.player1.dir.y * c.MOVE_SPEED

        if pygame.key.get_pressed()[c.P1_S]:
            pass

        """ Player 2 input """
        if pygame.key.get_pressed()[c.P2_L]:
            self.player2.rotation += c.TURN_SPEED

        if pygame.key.get_pressed()[c.P2_R]:
            self.player2.rotation -= c.TURN_SPEED

        if pygame.key.get_pressed()[c.P2_D]:
            self.player2.vel.x += self.player2.dir.x * c.MOVE_SPEED
            self.player2.vel.y += self.player2.dir.y * c.MOVE_SPEED

        if pygame.key.get_pressed()[c.P2_S]:
            pass


    def handle_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()


    def handle_move(self):
        for p in self.player_list:
            p.move()


    def handle_draw(self):
        self.screen.fill((100,90,100))

        for p in self.player_list:
            p.draw(self.screen)


        pygame.display.flip()



if __name__ == '__main__':
    spill = game()
    spill.run()