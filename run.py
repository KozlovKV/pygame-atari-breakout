import math
import pygame
import random
import sys


class Ball:
    def __init__(self, screen: pygame.Surface, image_name,
                 vector, x=400, y=300, r=50):
        self.screen = screen
        self.vector = list(vector)
        self.center_x = x
        self.center_y = y
        self.center_r = r
        self.img = pygame.image.load(image_name)
        self.img_rect = self.img.get_rect()

    def draw(self):
        self.move()
        self.img_rect.x = self.center_x - self.center_r
        self.img_rect.y = self.center_y - self.center_r
        self.screen.blit(self.img, self.img_rect)

    def move(self):
        self.center_x += self.vector[0]
        self.center_y += self.vector[1]
        if self.center_x < self.center_r or \
                self.center_x > self.screen.get_width() - self.center_r:
            self.vector[0] = -self.vector[0]
        if self.center_y < self.center_r or \
                self.center_y > self.screen.get_height() - self.center_r:
            self.vector[1] = -self.vector[1]


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    ball = Ball(screen, 'ball.png', (int(random.random() * 10) % 6,
                                     int(random.random() * 10) % 6))
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill((0, 0, 0))
        ball.draw()
        ball.move()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
