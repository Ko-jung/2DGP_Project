from Pokemon.pokemon import *
from pico2d import *
from random import *

class Machop (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Machop, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\machop.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Fight]

        self.BS_Hp   = 70
        self.BS_Atk  = 80
        self.BS_Def  = 50
        self.BS_Sp_A = 35
        self.BS_Sp_D = 35
        self.BS_Spd  = 35
        super(Machop, self).setValue()

        pass

    def update(self):
        super(Machop, self).update()
        pass

    def draw(self):
        super(Machop, self).draw()
        pass

    def handle_event(self, event):
        super(Machop, self).handle_event(event)
        pass