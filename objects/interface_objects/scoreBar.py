from objects.interface_objects.baseTextBar import TextBar
from constants import TICK


class ScoreBar(TextBar):
    def __init__(self, game, padding=5, x=0, y=0):
        super().__init__(game, x, y, 'SCORE: 0', padding,
                         (255, 255, 255), (0, 0, 0, 0))
        self.score_value = 0

    def score_up(self):
        self.score_value += 1
        new_str = f'SCORE: {self.score_value}'
        self.change_text(new_str)

    def get_score_value(self):
        return self.score_value
