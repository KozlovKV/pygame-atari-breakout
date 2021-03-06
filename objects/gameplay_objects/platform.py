from random import randint

import pygame

from constants import PLATFORM_COLLIDE_SOUND
from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject
from objects.gameplay_objects.helpPoint import HelpPoint


class Platform(BaseDrawableObject):
    def __init__(self, game, speed=8, color=(0x55, 0xDD, 0x33),
                 w=150, h=20):
        super().__init__(game, randint(0, game.WIDTH - w), game.HEIGHT - h - 5,
                         w, h, color)
        self.speed = speed
        self.vec_x = 0

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.vec_x += 1
            elif event.key == pygame.K_a:
                self.vec_x -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.vec_x -= 1
            elif event.key == pygame.K_a:
                self.vec_x += 1

    def collide_with_ball(self, ball):
        if super(Platform, self).collide_with_ball(ball):
            PLATFORM_COLLIDE_SOUND.play()
            ball.vector.change_x(self.vec_x)
            ball.move()
            ball.change_radius(-1)
            return True
        return False

    # def sides_collision(self, ball):
    #     p = (ball.center_x, ball.center_y + ball.radius)
    #     return self.rect.collidepoint(p)
    #
    # def angles_collision(self, ball):
    #     angles_points = [
    #         HelpPoint(self.rect.x, self.rect.y),
    #         HelpPoint(self.rect.x + self.rect.w, self.rect.y)
    #     ]
    #     for i in range(len(angles_points)):
    #         if pygame.sprite.collide_circle(ball, angles_points[i]):
    #             return True
    #     return False

    def logic(self):
        self.move()

    def move(self):
        new_x = self.rect.x + self.vec_x * self.speed
        if new_x > self.game.WIDTH - self.rect.w:
            new_x = self.game.WIDTH - self.rect.w
        elif new_x < 0:
            new_x = 0
        self.rect.x = new_x
