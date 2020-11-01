import pygame


class HelpPoint:
    def __init__(self, x, y):
        self.rect = pygame.rect.Rect(x, y, 1, 1)
        self.radius = 1