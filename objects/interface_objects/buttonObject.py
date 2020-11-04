import pygame

from constants import BUTTON_SOUND
from misc import is_point_in_rect, change_color
from objects.interface_objects.baseTextBar import TextBar


class ButtonObject(TextBar):
    def __init__(self, game, x=-1, y=-1, text='', padding=0,
                 text_color=(32, 32, 32), bg_color=(196, 96, 96)):
        super().__init__(game, x, y, text, padding, text_color, bg_color)
        self.is_pressed = False
        self.is_hover = False

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if is_point_in_rect(self.bg_rect, event.pos) and not self.is_hover:
                self.bg_color = change_color(self.bg_color, -32, -32, -32)
                self.is_hover = True
            elif not is_point_in_rect(self.bg_rect, event.pos) and \
                    self.is_hover:
                self.bg_color = change_color(self.bg_color, 32, 32, 32)
                self.is_hover = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_point_in_rect(self.bg_rect, event.pos):
                BUTTON_SOUND.play()
                self.is_pressed = True
