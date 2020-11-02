import pygame

from objects.gameplay_objects.helpPoint import HelpPoint


class BaseDrawableObject:
    def __init__(self, game, x, y, w, h, color):
        self.game = game
        self.color = color
        self.rect = pygame.rect.Rect(x, y, w, h)

    def events(self, event):
        pass

    def logic(self):
        pass

    def collide_with_ball(self, ball):
        if self.sides_collision(ball):
            return True
        if self.angles_collision(ball):
            return True
        return False

    def sides_collision(self, ball):
        ball_points = [
            (ball.center_x, ball.center_y - ball.radius),
            (ball.center_x + ball.radius, ball.center_y),
            (ball.center_x, ball.center_y + ball.radius),
            (ball.center_x - ball.radius, ball.center_y)
        ]
        for i in range(len(ball_points)):
            if self.rect.collidepoint(ball_points[i]):
                if i % 2 == 0:
                    ball.horizontal_collision_reaction()
                else:
                    ball.vertical_collision_reaction()
                return True
        return False
        '''
        Альтернативный вариант - записать в отдельный список определённые 
        стороны прямоугольника, чтобы проверять коллизию именно с ними
        '''

    def angles_collision(self, ball):
        angles_points = [
            HelpPoint(self.rect.x, self.rect.y),
            HelpPoint(self.rect.x + self.rect.w, self.rect.y),
            HelpPoint(self.rect.x + self.rect.w, self.rect.y + self.rect.h),
            HelpPoint(self.rect.x, self.rect.y + self.rect.h)
        ]
        for i in range(len(angles_points)):
            if pygame.sprite.collide_circle(ball, angles_points[i]):
                ball.angle_collision_reaction()
                return True
        return False
        '''
        Альтерантивный вариант - проверять коллизию с шариком как 
        прямоугольник-точка и затем проверять расстояние от точки до центра
        '''
        # angles_points = [
        #     (self.rect.x, self.rect.y),
        #     (self.rect.x + self.rect.w, self.rect.y),
        #     (self.rect.x + self.rect.w, self.rect.y + self.rect.h),
        #     (self.rect.x, self.rect.y + self.rect.h)
        # ]

    def undraw(self):
        self.color = pygame.color.Color(0, 0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
