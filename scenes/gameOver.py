import pygame

from objects.interface_objects.baseTextBar import TextBar
from objects.interface_objects.highScoreBar import HighScoreTable
from objects.interface_objects.inputBar import InputBar
from scenes.base import BaseScene


class GameOverScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.h_score_name = InputBar(game)
        self.objects.append(self.h_score_name)
        self.game_over_msg = TextBar(game, -1, 60, 'GAME OVER', 4,
                                     (0, 0, 0), (0xAA, 0, 0), True)
        self.objects.append(self.game_over_msg)
        self.h_score_table = HighScoreTable(game)
        self.objects.append(self.h_score_table)

    def events(self):
        super(GameOverScene, self).events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_over = True

    def logic(self):
        if self.h_score_name.input_end:
            result = self.h_score_name.get_content()
            score = self.game.score
            self.h_score_table.add_new_score(f'{result} {score}')

    def draw(self):
        if not self.h_score_name.input_end:
            self.h_score_name.draw()
        else:
            super(GameOverScene, self).draw()
