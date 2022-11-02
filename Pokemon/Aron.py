import Pokemon as P
from pico2d import *

class Aron (P.Pokemon):
    def __init__(self, x = None, y = None):
        # self.image = load_image('Pokemon\\Image\\Aron.png')
        # self.x = x
        # self.y = y
        # self.direct = 0
        # self.frame = 0
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = P.DIR_S
        self.fullFrame = 3
        self.image = load_image('Aron.png')

    def update(self):
        self.frame = (self.frame+1) % self.fullFrame

    def draw(self):
        self.image.clip_draw(1 + 29 * self.frame, 1 + 29 * self.direct, 28, 28, self.x, self.y, 28*2, 28*2)
        pass
