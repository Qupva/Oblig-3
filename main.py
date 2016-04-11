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

        self.time = 1

        heart_img = pygame.image.load(c.HEART_FNAME).convert_alpha()
        p1_txt = pygame.image.load(c.P1_TXT).convert_alpha()
        p2_txt = pygame.image.load(c.P2_TXT).convert_alpha()

        self.heart_image = pygame.transform.scale(heart_img, (c.HEART_SIZE, c.HEART_SIZE))
        self.p1_text = pygame.transform.scale(p1_txt, (int(c.GAME_SCALE * 10.5), c.GAME_SCALE * 2))
        self.p2_text = pygame.transform.scale(p2_txt, (int(c.GAME_SCALE * 10.5), c.GAME_SCALE * 2))

        self.player_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        self.player1 = player1(self, (c.GAME_SCALE * 2), (c.SCREEN_Y // 2))
        self.player2 = player2(self, (c.SCREEN_X - c.GAME_SCALE * 5), (c.SCREEN_Y // 2))

        self.player_list.add(self.player1)
        self.player_list.add(self.player2)

    def run(self):
        self.clock = pygame.time.Clock()
        
        while True:
            self.time_passed = self.clock.tick(60)
            self.time_passed_seconds = self.time_passed / 1000.0

            self.handle_event()

            if self.time:
                self.player_input()
                self.handle_move()

            self.handle_draw()

    def player_input(self):
    
        """ Player 1 input """
        if pygame.key.get_pressed()[c.P1_L]:
            self.player1.rotation += c.TURN_SPEED

        if pygame.key.get_pressed()[c.P1_R]:
            self.player1.rotation -= c.TURN_SPEED

        if pygame.key.get_pressed()[c.P1_D]:
            self.player1.vel.x += self.player1.dir.x * c.MOVE_SPEED * 0.6
            self.player1.vel.y += self.player1.dir.y * c.MOVE_SPEED

        if pygame.key.get_pressed()[c.P1_S]:
            if self.player1.bullet_timer >= c.FIRE_RATE:
                self.player1.weapon.fire(self, self.player1)
                self.player1.bullet_timer = 0
            else:
                self.player1.bullet_timer += self.time_passed_seconds

        """ Player 2 input """
        if pygame.key.get_pressed()[c.P2_L]:
            self.player2.rotation += c.TURN_SPEED

        if pygame.key.get_pressed()[c.P2_R]:
            self.player2.rotation -= c.TURN_SPEED

        if pygame.key.get_pressed()[c.P2_D]:
            self.player2.vel.x += self.player2.dir.x * c.MOVE_SPEED * 0.6
            self.player2.vel.y += self.player2.dir.y * c.MOVE_SPEED

        if pygame.key.get_pressed()[c.P2_S]:
            if self.player2.bullet_timer >= c.FIRE_RATE:
                self.player2.weapon.fire(self, self.player2)
                self.player2.bullet_timer = 0
            else:
                self.player2.bullet_timer += self.time_passed_seconds


    def handle_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if pygame.key.get_pressed()[c.TIME_TOGGLE]:
            if self.time == 1:
                self.time = 0
            else:
                self.time = 1

        for player in self.player_list:
            if pygame.sprite.spritecollideany(player, self.bullet_list):
                obj = pygame.sprite.spritecollideany(player, self.bullet_list)
                obj.on_hit()
                player.health -= 1
            if not player.health:
                player.kill()


    def handle_move(self):

        for p in self.player_list:
            p.move()

        for b in self.bullet_list:
            b.move(self)


    def handle_draw(self):
        self.screen.fill((c.BG_COLOR))


        self.bullet_list.draw(self.screen)
        self.player_list.draw(self.screen)


        self.screen.blit(self.p1_text, (0, 5))
        self.screen.blit(self.p2_text, (int(c.SCREEN_X - c.GAME_SCALE * 10.5), 5))

        x, n = 0, 0

        while n < self.player1.health:
            self.screen.blit(self.heart_image, (x, c.GAME_SCALE * 3))
            x += c.HEART_SIZE
            n += 1

        n = 0
        x = c.SCREEN_X - c.GAME_SCALE * 5

        while n < self.player2.health:
            self.screen.blit(self.heart_image, (x, c.GAME_SCALE * 3))
            x -= c.HEART_SIZE
            n += 1

        pygame.display.flip()



if __name__ == '__main__':
    spill = game()
    spill.run()