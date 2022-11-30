from Pokemon.aipokemon import AiPokemon
from Pokemon.pokemon import *
from pico2d import *
from random import *


class Sunkern (AiPokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Sunkern, self).__init__()
        self.x, self.y = XY[0], XY[1]
        print(f'Sunkern {self.x, self.y = }')
        self.image = load_image('Pokemon\\Image\\sunkern.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Grass]

        self.BS_Hp = 30
        self.BS_Atk = 30
        self.BS_Def = 30
        self.BS_Sp_A = 30
        self.BS_Sp_D = 30
        self.BS_Spd = 30

        super(Sunkern, self).setValue()
        pass

    def update(self):
        super(Sunkern, self).update()
        pass

    def draw(self):
        super(Sunkern, self).draw()
        pass

    def handle_event(self, event):
        super(Sunkern, self).handle_event(event)
        pass