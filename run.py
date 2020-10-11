import pygame
import random
import sys


class Platform:
    def __init__(self, screen: pygame.Surface, speed=8, x=10, y=570,
                 color=(0x55, 0xDD, 0x33), w=200, h=20):
        self.screen = screen
        self.speed = speed
        self.color = color
        self.rect = pygame.draw.rect(screen, color, (x, y, w, h))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self, vec_x):
        if vec_x > 0 and vec_x + self.rect.x + self.rect.w > 800:
            vec_x = 0
        elif vec_x < 0 and vec_x + self.rect.x < 0:
            vec_x = 0
        self.rect = self.rect.move(vec_x * self.speed, 0)


class Ball:
    def __init__(self, screen: pygame.Surface, image_name,
                 vector, x=400, y=300, r=50):
        self.screen = screen
        self.vector = list(vector)
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.img = pygame.image.load(image_name)
        self.img_rect = self.img.get_rect()

    def draw(self):
        self.screen.blit(self.img, self.img_rect)

    def move(self):
        self.center_x += self.vector[0]
        self.center_y += self.vector[1]
        if self.center_x < self.radius or \
                self.center_x > self.screen.get_width() - self.radius:
            self.vector[0] = -self.vector[0]
        if self.center_y < self.radius or \
                self.center_y > self.screen.get_height() - self.radius:
            self.vector[1] = -self.vector[1]
        self.img_rect.x = self.center_x - self.radius
        self.img_rect.y = self.center_y - self.radius

    def collision_with_platform(self, p: Platform):
        if p.rect.x <= self.center_x <= p.rect.x + p.rect.w and \
                self.center_y + self.radius >= p.rect.y:
            self.vector[1] = -self.vector[1]


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    ball = Ball(screen, 'ball.png', (int(random.random() * 10) % 6,
                                     int(random.random() * 10) % 6))

    p = Platform(screen)
    p_move = 0

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

        screen.fill((0, 0, 0))
        ball.draw()
        p.draw()

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
