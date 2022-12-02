from Pokemon.pokemon import *
from pico2d import *
from random import *


class Totodile (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Totodile, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\totodile.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Water]

        self.BS_Hp = 50
        self.BS_Atk = 65
        self.BS_Def = 64
        self.BS_Sp_A = 44
        self.BS_Sp_D = 48
        self.BS_Spd = 43
        super(Totodile, self).setValue()

        pass

    def update(self):
        super(Totodile, self).update()
        pass

    def draw(self):
        super(Totodile, self).draw()
        pass

    def handle_event(self, event):
        super(Totodile, self).handle_event(event)
        pass