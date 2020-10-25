import pygame


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