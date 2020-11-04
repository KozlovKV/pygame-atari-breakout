import random

import pygame

from objects.gameplay_objects.ball import Ball
from objects.gameplay_objects.bricksTableObject import BricksTableObject
from objects.gameplay_objects.platform import Platform
from objects.interface_objects.scoreBar import ScoreBar
from scenes.base import BaseScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.ball = Ball(game, (random.choice([1, -1]) * random.randint(2, 4),
                                -random.randint(2, 4)))
        self.objects.append(self.ball)
        self.moving_platform = Platform(game)
        self.objects.append(self.moving_platform)

        self.bricks = BricksTableObject(game)
        self.objects.append(self.bricks)

        self.score_bar = ScoreBar(game)
        self.objects.append(self.score_bar)

    def events(self, event):
        super(GameScene, self).events(event)
        if self.game.any_exit_command(event):
            self.game_over(-1)

    def logic(self):
        super(GameScene, self).logic()
        self.moving_platform.collide_with_ball(self.ball)
        if self.ball.is_game_over():
            self.game_over(-1)
        if self.bricks.is_win():
            self.game_over(1)

    def game_over(self, status):
        self.game.game_status = status
        self.game.score = self.score_bar.get_score_value()
        self.game.change_scene(self.game.SCENE_GAME_OVER)
