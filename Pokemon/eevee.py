from Pokemon.pokemon import *
from pico2d import *
from random import *

class Eevee (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Eevee, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\eevee.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Normal]

        self.BS_Hp   = 55
        self.BS_Atk  = 55
        self.BS_Def  = 50
        self.BS_Sp_A = 45
        self.BS_Sp_D = 65
        self.BS_Spd  = 55
        super(Eevee, self).setValue()

        pass

    def update(self):
        super(Eevee, self).update()
        pass

    def draw(self):
        super(Eevee, self).draw()
        pass

    def handle_event(self, event):
        super(Eevee, self).handle_event(event)
        pass