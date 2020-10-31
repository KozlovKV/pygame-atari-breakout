import pygame

from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject


class Platform(BaseDrawableObject):
    def __init__(self, game, speed=10, x=10, y=550, color=(0x55, 0xDD, 0x33),
                 w=200, h=20):
        super().__init__(game)
        self.speed = speed
        self.vec_x = 0
        self.color = color
        self.rect = pygame.draw.rect(self.game.screen, color, (x, y, w, h))

    def events(self):
        for event in pygame.event.get():
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

    def logic(self):
        self.move()

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)

    def move(self):
        new_x = self.rect.x + self.vec_x * self.speed
        if new_x > self.game.WIDTH - self.rect.w:
            new_x = self.game.WIDTH - self.rect.w
        elif new_x < 0:
            new_x = 0
        self.rect.x = new_x
