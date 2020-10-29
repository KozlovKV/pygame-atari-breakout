import pygame


class Game:
    SIZE = WIDTH, HEIGHT = 800, 600
    SCENE_MENU = 0
    SCENE_GAME = 1
    SCENE_GAME_OVER = 2

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
