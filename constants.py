import pygame


TICK = 10

pygame.font.init()
MAIN_FONT = pygame.font.SysFont('Consolas', 32, True)

pygame.mixer.init()
BUTTON_SOUND = pygame.mixer.Sound('sound/button.wav')
BRICK_COLLIDE_SOUND = pygame.mixer.Sound('sound/brick_collide.wav')
PLATFORM_COLLIDE_SOUND = pygame.mixer.Sound('sound/platform_collide.wav')
WIN_SOUND = pygame.mixer.Sound('sound/win.wav')
GAME_OVER_SOUND = pygame.mixer.Sound('sound/game_over.wav')
