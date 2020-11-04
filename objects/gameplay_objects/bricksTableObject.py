from functools import reduce

from misc import get_random_color
from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject


class BricksTableObject:
    def __init__(self, game, width_count=10, height_count=5,
                 brick_width=70, brick_height=40, padding=50, infinite=False):
        self.game = game
        self.table = [[]] * height_count
        for i in range(height_count-1, -1, -1):
            for j in range(width_count):
                x = padding + brick_width * j
                y = padding + brick_height * i
                self.table[i].append(
                    BaseDrawableObject(game, x, y, brick_width, brick_height,
                                       get_random_color((0, 0, 0))))

    def events(self, event):
        pass

    def logic(self):
        ball = self.game.scenes[self.game.SCENE_GAME].ball
        score_bar = self.game.scenes[self.game.SCENE_GAME].score_bar
        for line in self.table:
            i = 0
            while i < len(line):
                if line[i].collide_with_ball(ball):
                    score_bar.score_up()
                    line.pop(i)
                    i -= 1
                i += 1

    def is_win(self):
        return self.get_bricks_count() == 0 and not self.game.infinite

    def get_bricks_count(self):
        sum = 0
        for line in self.table:
            sum += len(line)
        return sum

    def add_new_line(self):
        pass

    def draw(self):
        for line in self.table:
            for brick in line:
                brick.draw()
