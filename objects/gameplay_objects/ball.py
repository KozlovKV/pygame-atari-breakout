from random import randint, choice

import pygame

from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject
from objects.gameplay_objects.speedVector import SpeedVector


class Ball(BaseDrawableObject):
    def __init__(self, game, vector, color=(196, 32, 32), x=400, y=500, r=35,
                 min_r=25):
        super().__init__(game, x-r, y-r, 2*r, 2*r, color)
        self.vector = SpeedVector(vector[0], vector[1])
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.min_radius = min_r
        self.border_collision = False

    def logic(self):
        self.move()

    def move(self):
        self.center_x += self.vector.get_x()
        self.center_y += self.vector.get_y()
        if self.center_x < self.radius or \
                self.center_x > self.game.screen.get_width() - self.radius:
            self.vector.invert_x()
            self.center_x += self.vector.get_x()
            self.center_y += self.vector.get_y()
        if self.center_y < self.radius:
            self.vector.invert_y()
            self.center_x += self.vector.get_x()
            self.center_y += self.vector.get_y()
        self.rect.x = self.center_x - self.radius
        self.rect.y = self.center_y - self.radius

    def horizontal_collision_reaction(self):
        cos_ = self.vector.x / self.vector.y
        self.vector.invert_y()
        self.vector.change_vector(choice((-0.5, 0, 0.5)))
        self.vector.multiply(cos_ + 0.25)

    def vertical_collision_reaction(self):
        cos_ = self.vector.y / self.vector.x
        self.vector.invert_x()
        self.vector.change_vector(choice((-0.5, 0, 0.5)))
        self.vector.multiply(cos_ + 0.1)

    def angle_collision_reaction(self):
        self.vector.invert_vector()
        self.vector.change_vector(0.5)

    def change_radius(self, delta):
        self.radius += delta
        self.radius = self.radius if self.radius >= self.min_radius \
            else self.min_radius

    def is_game_over(self):
        return self.center_y + self.radius >= self.game.HEIGHT + 3

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color,
                           (self.center_x, self.center_y), self.radius)