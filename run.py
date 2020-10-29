import random
import sys

from objects.interface_objects.baseTextBar import TextBar
from constants import *

from objects.interface_objects.scoreBar import ScoreBar
from objects.interface_objects.inputBar import InputBar
from objects.interface_objects.highScoreBar import HighScoreTable

from objects.gameplay_objects.platform import Platform
from objects.gameplay_objects.ball import Ball


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    ball = Ball(screen, 'ball.png', (random.choice([1, -1]) * 2, -2))

    p = Platform(screen)
    p_move = 0

    score = ScoreBar(screen, 5)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    p_move += 1
                elif event.key == pygame.K_a:
                    p_move -= 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    p_move -= 1
                elif event.key == pygame.K_a:
                    p_move += 1

        ball.move()
        p.move(p_move)
        ball.collision_with_platform(p)
        score.do_tick()

        screen.fill((0, 0, 0))
        ball.draw()
        p.draw()
        score.draw()

        if ball.is_game_over():
            game_over = True

            high_score_name = InputBar(screen, 'WRITE YOUR NICKNAME')
            high_score_name.input_process()
            screen.fill((0, 0, 0))
            result = high_score_name.get_content()

            game_over_msg = TextBar(screen, -1, 60, 'GAME OVER', 4,
                                    (0, 0, 0), (0xAA, 0, 0), True)
            game_over_msg.draw()
            high_score = HighScoreTable(screen)
            high_score.add_new_score(f'{result} {score.get_score_value()}')
            high_score.draw()

        pygame.display.flip()
        pygame.time.wait(TICK if not game_over else 2000)
    sys.exit()


if __name__ == '__main__':
    main()
