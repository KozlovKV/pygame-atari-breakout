import pygame
import sys

from objects.gameObject import Game


def main():
    pygame.init()
    game = Game()
    game.main_loop()
    sys.exit()


if __name__ == '__main__':
    main()
