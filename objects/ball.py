import pygame

from objects.helpPoint import CollisionHelperPointrect
from objects.platform import Platform


class Ball:
    def __init__(self, screen: pygame.Surface, image_name,
                 vector, x=400, y=300, r=50):
        self.screen = screen
        self.vector = list(vector)
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.img = pygame.image.load(image_name)
        self.rect = self.img.get_rect()
        self.left_collision = False
        self.right_collision = False

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def move(self):
        self.center_x += self.vector[0]
        self.center_y += self.vector[1]
        if self.center_x < self.radius or \
                self.center_x > self.screen.get_width() - self.radius:
            self.vector[0] = -self.vector[0]
        if self.center_y < self.radius:
            self.vector[1] = -self.vector[1]
        self.rect.x = self.center_x - self.radius
        self.rect.y = self.center_y - self.radius

    def collision_with_platform(self, p: Platform):
        left_angle = CollisionHelperPointrect(p.rect.x, p.rect.y)
        right_angle = CollisionHelperPointrect(p.rect.right, p.rect.y)
        # top collision
        if p.rect.collidepoint(self.center_x, self.center_y + self.radius) and \
                not self.center_y > p.rect.y:
            self.vector[1] = -self.vector[1]
            self.left_collision = False
            self.right_collision = False
        # collision lateral sides
        elif (p.rect.collidepoint(self.center_x + self.radius, self.center_y)
              or p.rect.collidepoint(self.center_x - self.radius,
                                     self.center_y)) and \
                not p.rect.x < self.center_x < p.rect.right:
            self.vector[0] = -self.vector[0]
            self.left_collision = False
            self.right_collision = False
        # collision with angles
        elif pygame.sprite.collide_circle(self, left_angle) and \
                not self.left_collision:
            self.vector = list(map(lambda x: -x, self.vector))
            self.left_collision = True
            self.right_collision = False
        elif pygame.sprite.collide_circle(self, right_angle) and \
                not self.right_collision:
            self.vector = list(map(lambda x: -x, self.vector))
            self.left_collision = False
            self.right_collision = True

    def is_game_over(self):
        return self.center_y >= self.screen.get_height()