import pygame
from constants import *


class TextBar:
    def __init__(self, game, x, y, text, padding=0,
                 text_color=(255, 255, 255), bg_color=(0, 0, 0)):
        self.game = game
        self.text = text
        self.padding = padding
        self.text_color = text_color
        self.bg_color = bg_color
        self.center_x = x == -1
        self.center_y = y == -1

        self.text_w, self.text_h = MAIN_FONT.size(text)
        self.x = x if not self.center_x else \
            (self.game.screen.get_width() - self.text_w) / 2 - padding
        self.y = y if not self.center_y else \
            (self.game.screen.get_height() - self.text_h) / 2 - padding
        self.bg_rect, self.rendered_text = [None] * 2
        self.change_text(text)

    def change_text(self, text):
        self.text = text
        self.text_w, self.text_h = MAIN_FONT.size(text)
        if self.center_x:
            self.x = (self.game.screen.get_width() - self.text_w) \
                     / 2 - self.padding
        if self.center_y:
            self.y = (self.game.screen.get_height() - self.text_h) \
                     / 2 - self.padding
        self.bg_rect = pygame.rect.Rect(self.x, self.y,
                                        self.text_w + self.padding * 2,
                                        self.text_h + self.padding * 2)
        self.rendered_text = MAIN_FONT.render(self.text, True, self.text_color)

    def events(self, event):
        pass

    def logic(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, self.bg_color, self.bg_rect)
        self.game.screen.blit(self.rendered_text, (self.x + self.padding,
                                                   self.y + self.padding,
                                                   self.text_w, self.text_h))
