import pygame

from bars.baseTextBar import TextBar

from constants import TICK, MAIN_FONT


class InputBar():
    def __init__(self, screen, label='', x=-1, y=260, length=3):
        self.screen = screen
        self.label = TextBar(screen, x, y, label, 4,
                             (255, 255, 255), (64, 64, 64), x == -1, y == -1) \
            if label != '' else ''
        self.content = [' '] * length
        self.content_index = 0
        self.input = TextBar(screen, x, y + 40, ''.join(self.content), 4,
                             (255, 255, 255), (64, 64, 64), x == -1, y == -1)

    def input_process(self):
        end_process = False

        cursor = True
        cursor_rect = pygame.rect.Rect(self.input.x + self.input.padding,
                       self.input.y + self.input.padding,
                       2, 32)

        while not end_process:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.content_index > 0:
                            self.content_index -= 1
                            self.content[self.content_index] = ' '
                            cursor_rect.x -= MAIN_FONT.size(' ')[0]
                    elif event.key == pygame.K_RETURN or \
                            event.key == pygame.QUIT:
                        end_process = True
                    elif self.content_index < len(self.content) \
                            and (65 <= event.key <= 90 or
                                 97 <= event.key <= 122):
                        self.content[self.content_index] = \
                            chr(event.key).upper()
                        self.content_index += 1
                        cursor_rect.x += MAIN_FONT.size(' ')[0]
                    self.input.change_text(''.join(self.content))

            self.screen.fill((0, 0, 0))
            if self.label != '':
                self.label.draw()
            self.input.draw()
            pygame.draw.rect(self.screen,
                             (255, 255, 255) if cursor else (64, 64, 64),
                             cursor_rect)
            cursor = not cursor

            pygame.display.flip()
            pygame.time.wait(TICK * 25)

    def get_content(self):
        return ''.join(self.content)
