import pygame

from objects.interface_objects.baseTextBar import TextBar
from objects.interface_objects.buttonObject import ButtonObject
from scenes.base import BaseScene


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.header = TextBar(game, -1, 80, 'ATARI BREAKOUT (ALMOST)')
        self.objects.append(self.header)
        self.btn_start = ButtonObject(game, -1, 180, 'PLAY CLASSIC', 14,
                                      (32, 32, 32), (196, 96, 32))
        self.objects.append(self.btn_start)
        self.btn_start_inf = ButtonObject(game, -1, 280, 'PLAY INFINITE', 14,
                                          (32, 32, 32), (196, 96, 32))
        self.objects.append(self.btn_start_inf)
        self.btn_exit = ButtonObject(game, -1, 380, 'EXIT', 14, (32, 32, 32),
                                     (196, 96, 32))
        self.objects.append(self.btn_exit)

    def events(self, event):
        super(MenuScene, self).events(event)
        if self.game.any_exit_command(event):
            self.game.game_over = True

    def logic(self):
        pygame.mixer.music.set_volume(0.5)
        if self.btn_start.is_pressed:
            self.btn_start.is_pressed = False
            self.game.infinite = False
            self.game.change_scene(self.game.SCENE_GAME)
        if self.btn_start_inf.is_pressed:
            self.btn_start.is_pressed = False
            self.game.infinite = True
            self.game.change_scene(self.game.SCENE_GAME)
        if self.btn_exit.is_pressed:
            self.btn_start.is_pressed = False
            self.game.game_over = True
