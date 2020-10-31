import pygame

from constants import TICK

from scenes.game import GameScene
from scenes.gameOver import GameOverScene
from scenes.menu import MenuScene


class Game:
    SIZE = WIDTH, HEIGHT = 800, 600
    # SCENE_MENU = 0
    SCENE_GAME = 0
    SCENE_GAME_OVER = 1

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SIZE)
        self.cur_scene_index = 0
        self.scenes = [
            # MenuScene(self),
            GameScene(self),
            GameOverScene(self)
        ]
        self.game_over = False
        self.input_time = False
        self.score = 0

    def main_loop(self):
        while not self.game_over:
            self.all_events()
            self.all_logic()
            self.all_draw()
            pygame.time.wait(TICK)

    def all_events(self):
        self.scenes[self.cur_scene_index].events()

    def all_logic(self):
        self.scenes[self.cur_scene_index].logic()

    def all_draw(self):
        self.screen.fill((0, 0, 0))
        self.scenes[self.cur_scene_index].draw()
        pygame.display.flip()

    def change_scene(self, index):
        self.cur_scene_index = index
