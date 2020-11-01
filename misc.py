import pygame


def is_point_in_rect(rect: pygame.rect.Rect, point: tuple):
    return rect.x <= point[0] <= rect.x + rect.w and \
           rect.y <= point[1] <= rect.y + rect.h


def change_color(previous_color, r, g, b):
    new_color = [
        previous_color[0] + r,
        previous_color[1] + g,
        previous_color[2] + b
    ]
    for i in range(len(new_color)):
        if new_color[i] < 0:
            new_color[i] = 0
        elif new_color[i] > 255:
            new_color[i] = 255
    return pygame.color.Color(new_color)
