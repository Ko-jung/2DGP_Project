from Pokemon.aipokemon import *
from Pokemon.pokemon import *
from pico2d import *
from random import *


class Wurmple (AiPokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Wurmple, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\wurmple.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Bug]

        self.BS_Hp = 45
        self.BS_Atk = 45
        self.BS_Def = 35
        self.BS_Sp_A = 20
        self.BS_Sp_D = 30
        self.BS_Spd = 20

        self.fullFrame = 2

        super(Wurmple, self).setValue()
        pass

    def update(self):
        super(Wurmple, self).update()
        pass

    def draw(self):
        super(Wurmple, self).draw()
        pass

    def handle_event(self, event):
        super(Wurmple, self).handle_event(event)
        pass