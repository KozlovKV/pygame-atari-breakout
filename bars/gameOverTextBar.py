from bars.baseTextBar import TextBar
from constants import MAIN_FONT


class GameOverTextBar(TextBar):
    def __init__(self, screen, text):
        w, h = MAIN_FONT.size(text)
        x = (screen.get_width() - w) / 2 - 10
        y = (screen.get_height() - h) / 2 - 10
        super().__init__(screen, x, y, text, 10, (0, 0, 0), (0xAA, 0, 0))