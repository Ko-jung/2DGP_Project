from Pokemon.pokemon import *
from pico2d import *
from random import *

class Plusle (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Plusle, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\plusle.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Elect]

        self.BS_Hp   = 60
        self.BS_Atk  = 50
        self.BS_Def  = 40
        self.BS_Sp_A = 85
        self.BS_Sp_D = 75
        self.BS_Spd  = 95
        super(Plusle, self).setValue()

        pass

    def update(self):
        super(Plusle, self).update()
        pass

    def draw(self):
        super(Plusle, self).draw()
        pass

    def handle_event(self, event):
        super(Plusle, self).handle_event(event)
        pass