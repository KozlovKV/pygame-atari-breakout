import pygame
from constants import *


class TextBar:
    def __init__(self, screen, x, y, text, padding=0,
                 text_color=(255, 255, 255), bg_color=(0, 0, 0),
                 center_x=False, center_y=False):
        self.screen = screen
        self.text = text
        self.padding = padding
        self.text_color = text_color
        self.bg_color = bg_color
        self.center_x = center_x
        self.center_y = center_y

        self.text_w, self.text_h = MAIN_FONT.size(text)
        self.x = x if not center_x else \
            (screen.get_width() - self.text_w) / 2 - padding
        self.y = y if not center_y else \
            (screen.get_height() - self.text_h) / 2 - padding
        self.bg_rect, self.rendered_text = [None] * 2
        self.change_text(text)

    def change_text(self, text):
        self.text = text
        self.text_w, self.text_h = MAIN_FONT.size(text)
        if self.center_x:
            self.x = (self.screen.get_width() - self.text_w) / 2 - self.padding
        if self.center_y:
            self.y = (self.screen.get_height() - self.text_h) / 2 - self.padding
        self.bg_rect = pygame.rect.Rect(self.x, self.y,
                                        self.text_w + self.padding * 2,
                                        self.text_h + self.padding * 2)
        self.rendered_text = MAIN_FONT.render(self.text, True, self.text_color)

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.bg_rect)
        self.screen.blit(self.rendered_text, (self.x + self.padding,
                                              self.y + self.padding,
                                              self.text_w, self.text_h))