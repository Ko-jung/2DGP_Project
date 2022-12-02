from Pokemon.pokemon import *
from pico2d import *
from random import *


class Treecko (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Treecko, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\treecko.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Grass]

        self.BS_Hp = 40
        self.BS_Atk = 45
        self.BS_Def = 35
        self.BS_Sp_A = 65
        self.BS_Sp_D = 55
        self.BS_Spd = 70
        super(Treecko, self).setValue()

        pass

    def update(self):
        super(Treecko, self).update()
        pass

    def draw(self):
        super(Treecko, self).draw()
        pass

    def handle_event(self, event):
        super(Treecko, self).handle_event(event)
        pass