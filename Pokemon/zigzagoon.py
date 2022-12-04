from Pokemon.pokemon import *
from pico2d import *
from random import *
from Pokemon.aipokemon import *


class Zigzagoon (AiPokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Zigzagoon, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\zigzagoon.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Normal]

        self.BS_Hp = 38
        self.BS_Atk = 30
        self.BS_Def = 41
        self.BS_Sp_A = 30
        self.BS_Sp_D = 41
        self.BS_Spd = 60

        super(Zigzagoon, self).setValue()
        pass

    def update(self):
        super(Zigzagoon, self).update()
        pass

    def draw(self):
        super(Zigzagoon, self).draw()
        pass

    def handle_event(self, event):
        super(Zigzagoon, self).handle_event(event)
        pass