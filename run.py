import pygame
import random
import sys


class CollisionHelperPointrect:
    def __init__(self, x, y):
        self.rect = pygame.rect.Rect(x, y, 1, 1)
        self.radius = 1


class Platform:
    def __init__(self, screen: pygame.Surface, speed=8, x=10, y=550,
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
        self.rect = self.img.get_rect()
        self.left_collision = False
        self.right_collision = False

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def move(self):
        self.center_x += self.vector[0]
        self.center_y += self.vector[1]
        if self.center_x < self.radius or \
                self.center_x > self.screen.get_width() - self.radius:
            self.vector[0] = -self.vector[0]
        if self.center_y < self.radius:
            self.vector[1] = -self.vector[1]
        self.rect.x = self.center_x - self.radius
        self.rect.y = self.center_y - self.radius

    def collision_with_platform(self, p: Platform):
        left_angle = CollisionHelperPointrect(p.rect.x, p.rect.y)
        right_angle = CollisionHelperPointrect(p.rect.right, p.rect.y)
        # top collision
        if p.rect.collidepoint(self.center_x, self.center_y + self.radius) and \
                not self.center_y > p.rect.y:
            self.vector[1] = -self.vector[1]
            self.left_collision = False
            self.right_collision = False
        # collision lateral sides
        elif (p.rect.collidepoint(self.center_x + self.radius, self.center_y)
                or p.rect.collidepoint(self.center_x - self.radius,
                                       self.center_y)) and \
                not p.rect.x < self.center_x < p.rect.right:
            self.vector[0] = -self.vector[0]
            self.left_collision = False
            self.right_collision = False
        # collision with angles
        elif pygame.sprite.collide_circle(self, left_angle) and \
                not self.left_collision:
            self.vector = list(map(lambda x: -x, self.vector))
            self.left_collision = True
            self.right_collision = False
        elif pygame.sprite.collide_circle(self, right_angle) and \
                not self.right_collision:
            self.vector = list(map(lambda x: -x, self.vector))
            self.left_collision = False
            self.right_collision = True

    def is_game_over(self):
        return self.center_y >= self.screen.get_height()


def main():
    pygame.init()
    pygame.font.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    main_font = pygame.font.SysFont('Consolas', 32, True)

    ball = Ball(screen, 'ball.png',
                (random.choice([1, -1]) * random.randint(3, 6),
                 -random.randint(3, 6)))

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

        if ball.is_game_over():
            game_over = True
            font_w, font_h = main_font.size('GAME OVER')
            font_x = (screen.get_width() - font_w) / 2
            font_y = (screen.get_height() - font_h) / 2
            game_over_rect = pygame.rect.Rect(font_x - 10, font_y - 10,
                                              font_w + 20, font_h + 20)
            game_over_msg = main_font.render('GAME OVER', True,
                                             (0, 0, 0))
            pygame.draw.rect(screen, (0xAA, 0, 0), game_over_rect)
            screen.blit(game_over_msg, (font_x, font_y, font_w, font_h))

        pygame.display.flip()
        pygame.time.wait(10 if not game_over else 2000)
    sys.exit()


if __name__ == '__main__':
    main()
