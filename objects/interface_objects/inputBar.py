import pygame

from objects.interface_objects.baseTextBar import TextBar

from constants import TICK, MAIN_FONT


class InputBar:
    def __init__(self, game, label='', x=-1, y=260, length=3):
        self.game = game
        self.label = TextBar(game, x, y, label, 4, (255, 255, 255),
                             (64, 64, 64)) if label != '' else ''
        self.content = [' '] * length
        self.content_index = 0
        self.input = TextBar(game, x, y + 40, ''.join(self.content), 4,
                             (255, 255, 255), (64, 64, 64))
        self.input_end = False
        self.cursor_rect = pygame.rect.Rect(self.input.x + self.input.padding,
                                            self.input.y + self.input.padding,
                                            2, 32)

    def events(self, event):
        if not self.input_end:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.content_index > 0:
                        self.content_index -= 1
                        self.content[self.content_index] = ' '
                        self.cursor_rect.x -= MAIN_FONT.size(' ')[0]
                elif event.key == pygame.K_RETURN or \
                        event.key == pygame.QUIT:
                    self.input_end = True
                    self.game.input_time = False
                elif self.content_index < len(self.content) \
                        and (65 <= event.key <= 90 or
                             97 <= event.key <= 122):
                    self.content[self.content_index] = \
                        chr(event.key).upper()
                    self.content_index += 1
                    self.cursor_rect.x += MAIN_FONT.size(' ')[0]
                self.input.change_text(''.join(self.content))

    def draw(self):
        if not self.input_end:
            if self.label != '':
                self.label.draw()
            self.input.draw()
            pygame.draw.rect(self.game.screen, (255, 255, 255),
                             self.cursor_rect)

    def get_content(self):
        return ''.join(self.content)
