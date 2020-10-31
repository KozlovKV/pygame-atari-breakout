class BaseScene:
    def __init__(self, game):
        self.game = game
        self.objects = []

    def events(self, event):
        for object in self.objects:
            object.events(event)

    def logic(self):
        for object in self.objects:
            object.logic()

    def draw(self):
        for object in self.objects:
            object.draw()
