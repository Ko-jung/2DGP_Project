from Pokemon.pokemon import *
from Pokemon.aipokemon import *
from pico2d import *
from random import *

class Minun (AiPokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Minun, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\minun.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Elect]

        self.BS_Hp   = 60
        self.BS_Atk  = 40
        self.BS_Def  = 50
        self.BS_Sp_A = 75
        self.BS_Sp_D = 85
        self.BS_Spd  = 95
        super(Minun, self).setValue()

        pass

    def update(self):
        super(Minun, self).update()
        pass

    def draw(self):
        super(Minun, self).draw()
        pass

    def handle_event(self, event):
        super(Minun, self).handle_event(event)
        pass