from Pokemon.pokemon import *
from pico2d import *
from random import *

class Cubone (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Cubone, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\cubone.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Ground]

        self.BS_Hp   = 50
        self.BS_Atk  = 50
        self.BS_Def  = 95
        self.BS_Sp_A = 40
        self.BS_Sp_D = 50
        self.BS_Spd  = 35
        super(Cubone, self).setValue()

        pass

    def update(self):
        super(Cubone, self).update()
        pass

    def draw(self):
        super(Cubone, self).draw()
        pass

    def handle_event(self, event):
        super(Cubone, self).handle_event(event)
        pass