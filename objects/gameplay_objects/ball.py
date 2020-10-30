import pygame

from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject
from objects.gameplay_objects.helpPoint import CollisionHelperPointrect
from objects.gameplay_objects.platform import Platform
from objects.gameplay_objects.speedVector import SpeedVector


class Ball(BaseDrawableObject):
    image_name = 'ball.png'

    def __init__(self, game, vector, x=400, y=300, r=50):
        super().__init__(game)
        self.vector = SpeedVector(vector[0], vector[1])
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.img = pygame.image.load(self.image_name)
        self.rect = self.img.get_rect()
        self.left_collision = False
        self.right_collision = False

    def logic(self):
        self.move()

    def move(self):
        self.center_x += self.vector.get_x()
        self.center_y += self.vector.get_y()
        if self.center_x < self.radius or \
                self.center_x > self.game.screen.get_width() - self.radius:
            self.vector.invert_x()
        if self.center_y < self.radius:
            self.vector.invert_y()
        self.rect.x = self.center_x - self.radius
        self.rect.y = self.center_y - self.radius

    def collision_with_platform(self, p: Platform):
        if self.top_collision(p) or self.side_collision(p) or \
                self.angles_collision(p):
            self.vector.speed_up()

    def top_collision(self, p: Platform):
        if p.rect.collidepoint(self.center_x, self.center_y + self.radius) and \
                not self.center_y > p.rect.y:
            self.vector.invert_y()
            self.left_collision = False
            self.right_collision = False
            return True
        return False

    def side_collision(self, p: Platform):
        if (p.rect.collidepoint(self.center_x + self.radius, self.center_y)
            or p.rect.collidepoint(self.center_x - self.radius,
                                   self.center_y)) and \
                not p.rect.x < self.center_x < p.rect.right:
            self.vector.invert_x()
            self.left_collision = False
            self.right_collision = False
            return True
        return False

    def angles_collision(self, p: Platform):
        left_angle = CollisionHelperPointrect(p.rect.x, p.rect.y)
        right_angle = CollisionHelperPointrect(p.rect.right, p.rect.y)
        if pygame.sprite.collide_circle(self, left_angle) and \
                not self.left_collision:
            self.vector.invert_vector()
            self.left_collision = True
            self.right_collision = False
            return True
        elif pygame.sprite.collide_circle(self, right_angle) and \
                not self.right_collision:
            self.vector.invert_vector()
            self.left_collision = False
            self.right_collision = True
            return True
        return False

    def is_game_over(self):
        return self.center_y >= self.game.screen.get_height()

    def draw(self):
        self.game.screen.blit(self.img, self.rect)
