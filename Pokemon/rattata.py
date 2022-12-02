from Pokemon.pokemon import *
from pico2d import *
from random import *


class Rattata (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Rattata, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\rattata.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Normal]

        self.BS_Hp = 30
        self.BS_Atk = 56
        self.BS_Def = 35
        self.BS_Sp_A = 25
        self.BS_Sp_D = 35
        self.BS_Spd = 72
        super(Rattata, self).setValue()

        pass

    def update(self):
        super(Rattata, self).update()
        pass

    def draw(self):
        super(Rattata, self).draw()
        pass

    def handle_event(self, event):
        super(Rattata, self).handle_event(event)
        pass