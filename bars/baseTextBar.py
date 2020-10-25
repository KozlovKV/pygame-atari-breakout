import pygame
from constants import *


class TextBar:
    def __init__(self, screen, x, y, text, padding=0,
                 text_color=(255, 255, 255), bg_color=(0, 0, 0)):
        self.screen = screen
        self.x = x  # for bg_rect
        self.y = y  # for bg_rect
        self.text = text
        self.padding = padding
        self.text_color = text_color
        self.bg_color = bg_color

        self.text_w, self.text_h, self.bg_rect, self.rendered_text = [None] * 4
        self.change_text(text)

    def change_text(self, text):
        self.text = text
        self.text_w, self.text_h = MAIN_FONT.size(text)
        self.bg_rect = pygame.rect.Rect(self.x, self.y,
                                        self.text_w + self.padding * 2,
                                        self.text_h + self.padding * 2)
        self.rendered_text = MAIN_FONT.render(self.text, True, self.text_color)

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.bg_rect)
        self.screen.blit(self.rendered_text, (self.x + self.padding,
                                              self.y + self.padding,
                                              self.text_w, self.text_h))