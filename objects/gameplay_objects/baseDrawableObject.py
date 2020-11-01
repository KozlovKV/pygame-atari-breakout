import pygame


class BaseDrawableObject:
    def __init__(self, game, x, y, w, h, color):
        self.game = game
        self.color = color
        self.rect = pygame.rect.Rect(x, y, w, h)

    def events(self, event):
        pass

    def logic(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
