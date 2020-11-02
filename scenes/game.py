import random

import pygame

from objects.gameplay_objects.ball import Ball
from objects.gameplay_objects.baseDrawableObject import BaseDrawableObject
from objects.gameplay_objects.platform import Platform
from objects.interface_objects.scoreBar import ScoreBar
from scenes.base import BaseScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.ball = Ball(game, (random.choice([1, -1]) * 2, -2))
        self.objects.append(self.ball)
        self.moving_platform = Platform(game)
        self.objects.append(self.moving_platform)

        self.bricks = [
            BaseDrawableObject(game, 25, 50, 75, 50, (32, 32, 32)),
            BaseDrawableObject(game, 100, 50, 75, 50, (32, 32, 196)),
            BaseDrawableObject(game, 175, 50, 75, 50, (32, 196, 32)),
            BaseDrawableObject(game, 250, 50, 75, 50, (32, 196, 196)),
            BaseDrawableObject(game, 325, 50, 75, 50, (196, 32, 32)),
            BaseDrawableObject(game, 400, 50, 75, 50, (196, 32, 196)),
            BaseDrawableObject(game, 475, 50, 75, 50, (196, 196, 32)),
            BaseDrawableObject(game, 550, 50, 75, 50, (196, 196, 196)),
            BaseDrawableObject(game, 625, 50, 75, 50, (32, 32, 196)),
            BaseDrawableObject(game, 700, 50, 75, 50, (32, 196, 32))
        ]
        self.brick_first_index = len(self.objects)
        self.objects += self.bricks

        self.score_bar = ScoreBar(game)
        self.objects.append(self.score_bar)

    def events(self, event):
        super(GameScene, self).events(event)
        if self.game.any_exit_command(event):
            self.game_over()

    def logic(self):
        super(GameScene, self).logic()
        self.moving_platform.collide_with_ball(self.ball)
        i = 0
        while i < len(self.bricks):
            if self.bricks[i].collide_with_ball(self.ball):
                self.score_bar.score_up()
                self.bricks.pop(i)
                self.objects.pop(self.brick_first_index + i)
                i -= 1
            i += 1
        if self.ball.is_game_over():
            self.game_over()

    def game_over(self):
        self.game.score = self.score_bar.get_score_value()
        self.game.change_scene(self.game.SCENE_GAME_OVER)
