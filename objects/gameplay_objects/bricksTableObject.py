from random import randint

from misc import get_random_color
from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject


class BricksTableObject:
    def __init__(self, game, width_count=10, height_count=5,
                 brick_width=70, brick_height=40, padding=50):
        self.game = game
        self.width_count = width_count
        self.height_count = height_count
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.padding = padding
        self.table = []
        for i in range(height_count):
            line = []
            for j in range(width_count):
                x = padding + brick_width * j
                y = padding + brick_height * i
                line.append(
                    BaseDrawableObject(game, x, y, brick_width, brick_height,
                                       get_random_color((0, 0, 0))))
            self.table.append(line)

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
        if self.game.infinite and self.get_bricks_count() <= 25:
            self.add_new_line()

    def is_win(self):
        return self.get_bricks_count() == 0 and not self.game.infinite

    def get_bricks_count(self):
        sum = 0
        for line in self.table:
            print(len(line))
            sum += len(line)
        return sum

    def add_new_line(self):
        for line in self.table:
            for brick in line:
                brick.rect.y += self.brick_height
        new_line = []
        for j in range(self.width_count):
            x = self.padding + self.brick_width * j
            y = self.padding
            new_line.append(
                BaseDrawableObject(self.game, x, y, self.brick_width,
                                   self.brick_height,
                                   get_random_color((0, 0, 0))))
        self.table.append(new_line)

    def draw(self):
        for line in self.table:
            for brick in line:
                brick.draw()
