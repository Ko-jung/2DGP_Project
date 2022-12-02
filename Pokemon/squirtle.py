from Pokemon.pokemon import *
from pico2d import *
from random import *


class Squirtle (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Squirtle, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\squirtle.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Water]

        self.BS_Hp = 44
        self.BS_Atk = 48
        self.BS_Def = 65
        self.BS_Sp_A = 50
        self.BS_Sp_D = 64
        self.BS_Spd = 43
        super(Squirtle, self).setValue()

        pass

    def update(self):
        super(Squirtle, self).update()
        pass

    def draw(self):
        super(Squirtle, self).draw()
        pass

    def handle_event(self, event):
        super(Squirtle, self).handle_event(event)
        pass