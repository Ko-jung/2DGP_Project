from Pokemon.pokemon import *
from pico2d import *
from random import *


class Psyduck (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Psyduck, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\psyduck.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Water]

        self.BS_Hp = 50
        self.BS_Atk = 52
        self.BS_Def = 48
        self.BS_Sp_A = 65
        self.BS_Sp_D = 50
        self.BS_Spd = 55

        super(Psyduck, self).setValue()

        pass

    def update(self):
        super(Psyduck, self).update()
        pass

    def draw(self):
        super(Psyduck, self).draw()
        pass

    def handle_event(self, event):
        super(Psyduck, self).handle_event(event)
        pass