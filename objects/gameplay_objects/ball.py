from random import randint

import pygame

from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject
from objects.gameplay_objects.speedVector import SpeedVector


class Ball(BaseDrawableObject):
    def __init__(self, game, vector, color=(196, 32, 32), x=400, y=400, r=25):
        super().__init__(game, x-r, y-r, 2*r, 2*r, color)
        self.vector = SpeedVector(vector[0], vector[1])
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.border_collision = False

    def logic(self):
        self.move()

    def move(self):
        self.center_x += self.vector.get_x()
        self.center_y += self.vector.get_y()
        if self.center_x < self.radius or \
                self.center_x > self.game.screen.get_width() - self.radius:
            if not self.border_collision:
                self.border_collision = True
                self.vector.invert_x()
            else:
                self.border_collision = False
        if self.center_y < self.radius \
                or self.center_y > self.game.screen.get_height() - self.radius:
            if not self.border_collision:
                self.border_collision = True
                self.vector.invert_y()
            else:
                self.border_collision = False
        self.rect.x = self.center_x - self.radius
        self.rect.y = self.center_y - self.radius

    def horizontal_collision_reaction(self):
        self.vector.invert_y()

    def vertical_collision_reaction(self):
        self.vector.invert_x()

    def angle_collision_reaction(self):
        self.vector.invert_vector()

    def change_radius(self, left, right):
        self.radius = randint(left, right)

    def is_game_over(self):
        # return False
        return self.center_y + self.radius >= self.game.HEIGHT + 3

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color,
                           (self.center_x, self.center_y), self.radius)