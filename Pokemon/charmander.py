from Pokemon.pokemon import *
from pico2d import *
from random import *

class Charmander (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Charmander, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\charmander.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Fire]

        self.BS_Hp   = 39
        self.BS_Atk  = 52
        self.BS_Def  = 43
        self.BS_Sp_A = 60
        self.BS_Sp_D = 50
        self.BS_Spd  = 65
        super(Charmander, self).setValue()

        pass

    def update(self):
        super(Charmander, self).update()
        pass

    def draw(self):
        super(Charmander, self).draw()
        pass

    def handle_event(self, event):
        super(Charmander, self).handle_event(event)
        pass