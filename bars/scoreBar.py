from bars.baseTextBar import TextBar
from constants import TICK


class ScoreBar(TextBar):
    def __init__(self, screen, x=0, y=0):
        super().__init__(screen, x, y, 'SCORE: 0', 10, (0, 0, 0), (0, 0xAA, 0))
        self.ticks_count = int(1000 / TICK)
        self.score_value = 0
        self.current_ticks_count = 0

    def do_tick(self):
        self.current_ticks_count += 1
        if self.current_ticks_count >= self.ticks_count:
            self.current_ticks_count = 0
            self.score_value += 1
            new_str = f'SCORE: {self.score_value}'
            self.change_text(new_str)