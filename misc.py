import random

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


def get_random_color(exception):
    color = random.choice(list(pygame.color.THECOLORS.values()))
    while abs(color[0] - exception[0]) < 32 or \
            abs(color[1] - exception[1]) < 32 or \
            abs(color[2] - exception[2]) < 32:
        color = random.choice(list(pygame.color.THECOLORS.values()))
    return color


def get_list_of_radius_points(center_x, center_y, r):
    res = []
    for x_sign in (-1, 1):
        for y_sign in (-1, 1):
            for x in range(0, r+1):
                y = int((r*r - x*x)**0.5)
                res.append((center_x + x * x_sign, center_y + y * y_sign))
    return res
