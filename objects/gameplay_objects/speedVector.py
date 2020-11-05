class SpeedVector:
    MAX = 6
    MIN = 2

    @staticmethod
    def change_one_coord(prev, delta):
        new_coord = prev + delta
        if new_coord < SpeedVector.MIN:
            new_coord = SpeedVector.MIN
        elif prev > SpeedVector.MAX:
            new_coord = SpeedVector.MAX
        return new_coord

    def __init__(self, x, y):
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

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def invert_x(self):
        self.x_move *= -1

    def invert_y(self):
        self.y_move *= -1

    def invert_vector(self):
        self.invert_x()
        self.invert_y()

    def multiply(self, k):  # 0.25 < k < 1.25
        self.x *= k
        self.y *= k

    def change_x(self, delta):
        self.x = SpeedVector.change_one_coord(self.x, delta)
        if self.x < 0:
            self.x = abs(self.x)
            self.x_move *= -1

    def change_y(self, delta):
        self.y = SpeedVector.change_one_coord(self.y, delta)
        if self.y < 0:
            self.y = abs(self.y)
            self.y_move *= -1

    def change_vector(self, delta):
        self.change_x(delta)
        self.change_y(delta)
