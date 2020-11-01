from objects.interface_objects.baseTextBar import TextBar
from objects.interface_objects.buttonObject import ButtonObject
from scenes.base import BaseScene


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.header = TextBar(game, -1, 100, 'ATARI BREAKOUT (ALMOST)')
        self.objects.append(self.header)
        self.btn_start = ButtonObject(game, -1, 220, 'PLAY', 14, (32, 32, 32),
                                      (196, 96, 32))
        self.objects.append(self.btn_start)
        self.btn_exit = ButtonObject(game, -1, 330, 'EXIT', 14, (32, 32, 32),
                                     (196, 96, 32))
        self.objects.append(self.btn_exit)

    def events(self, event):
        super(MenuScene, self).events(event)
        if self.game.any_exit_command(event):
            self.game.game_over = True

    def logic(self):
        if self.btn_start.is_pressed:
            self.btn_start.is_pressed = False
            self.game.change_scene(self.game.SCENE_GAME)
        if self.btn_exit.is_pressed:
            self.btn_start.is_pressed = False
            self.game.game_over = True
