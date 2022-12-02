from Pokemon.pokemon import *
from pico2d import *
from random import *


class Torchic (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Torchic, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\torchic.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Fire]

        self.BS_Hp = 45
        self.BS_Atk = 60
        self.BS_Def = 40
        self.BS_Sp_A = 70
        self.BS_Sp_D = 50
        self.BS_Spd = 45
        super(Torchic, self).setValue()

        pass

    def update(self):
        super(Torchic, self).update()
        pass

    def draw(self):
        super(Torchic, self).draw()
        pass

    def handle_event(self, event):
        super(Torchic, self).handle_event(event)
        pass