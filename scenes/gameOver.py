import pygame

from objects.interface_objects.baseTextBar import TextBar
from objects.interface_objects.highScoreBar import HighScoreTable
from objects.interface_objects.inputBar import InputBar
from scenes.base import BaseScene


class GameOverScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.h_score_name = InputBar(game, 'WRITE YOUR NICKNAME:')
        self.objects.append(self.h_score_name)
        self.game_over_msg = TextBar(game, -1, 60, 'GAME OVER', 4,
                                     (0, 0, 0), (0xAA, 0, 0), True)
        self.objects.append(self.game_over_msg)
        self.h_score_table = HighScoreTable(game)
        self.objects.append(self.h_score_table)

    def events(self, event):
        super(GameOverScene, self).events(event)
        if self.game.any_exit_command(event):
            self.game.game_over = True

    def logic(self):
        if self.h_score_name.input_end and \
                self.h_score_table.count_new_scores == 0:
            result = self.h_score_name.get_content()
            score = self.game.score
            self.h_score_table.add_new_score(f'{result} {score}')

    def draw(self):
        if not self.h_score_name.input_end:
            self.h_score_name.draw()
        else:
            super(GameOverScene, self).draw()
