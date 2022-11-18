from pico2d import *

class rect:
    def __init__(self, left, down, right, up):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_bb(self):
        return  self.left, self.down, self.right, self.up

    def draw(self):
        draw_rectangle(*(self.get_bb()))

    def handle_collision(self, other, group):
        pass