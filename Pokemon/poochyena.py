from Pokemon.pokemon import *
from pico2d import *
from random import *


class Poochyena (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Poochyena, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\poochyena.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Dark]

        self.BS_Hp = 35
        self.BS_Atk = 55
        self.BS_Def = 35
        self.BS_Sp_A = 30
        self.BS_Sp_D = 30
        self.BS_Spd = 35
        super(Poochyena, self).setValue()

        pass

    def update(self):
        super(Poochyena, self).update()
        pass

    def draw(self):
        super(Poochyena, self).draw()
        pass

    def handle_event(self, event):
        super(Poochyena, self).handle_event(event)
        pass