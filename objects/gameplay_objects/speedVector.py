class SpeedVector:
    def __init__(self, x, y, max_=6):
        self.max_speed = max_
        self.x_move = -1 if x < 0 else 1
        self.y_move = -1 if y < 0 else 1
        self.x = abs(x)
        self.y = abs(y)

    def get_x(self):
        return self.x * self.x_move

    def get_y(self):
        return self.y * self.y_move

    def get_vector(self):
        return self.get_x(), self.get_y()

    def invert_x(self):
        self.x_move *= -1

    def invert_y(self):
        self.y_move *= -1

    def invert_vector(self):
        self.invert_x()
        self.invert_y()

    def change_x(self, delta):
        self.x += delta

    def change_y(self, delta):
        self.y += delta

    def speed_up(self, delta=1):
        self.x = self.x + delta \
            if self.x + delta <= self.max_speed else self.max_speed
        self.y = self.y + delta \
            if self.y + delta <= self.max_speed else self.max_speed

    def speed_down(self, delta=1):
        self.x -= delta
        self.y -= delta
        self.__init__(self.x, self.y)
