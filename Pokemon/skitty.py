from Pokemon.pokemon import *
from pico2d import *
from random import *


class Skitty (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Skitty, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\skitty.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Normal]

        self.BS_Hp = 70
        self.BS_Atk = 65
        self.BS_Def = 65
        self.BS_Sp_A = 55
        self.BS_Sp_D = 55
        self.BS_Spd = 70
        super(Skitty, self).setValue()

        pass

    def update(self):
        super(Skitty, self).update()
        pass

    def draw(self):
        super(Skitty, self).draw()
        pass

    def handle_event(self, event):
        super(Skitty, self).handle_event(event)
        pass