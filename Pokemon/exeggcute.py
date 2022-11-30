from Pokemon.aipokemon import *
from Pokemon.pokemon import *
from pico2d import *
from random import *

class Exeggcute (AiPokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Exeggcute, self).__init__()
        self.x, self.y = XY[0], XY[1]
        print(f'Exeggcute {self.x, self.y = }')
        self.image = load_image('Pokemon\\Image\\exeggcute.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Grass, Type_Psy]

        self.BS_Hp   = 60
        self.BS_Atk  = 40
        self.BS_Def  = 80
        self.BS_Sp_A = 60
        self.BS_Sp_D = 45
        self.BS_Spd  = 40

        super(Exeggcute, self).setValue()

        pass

    def update(self):
        super(Exeggcute, self).update()
        pass

    def draw(self):
        super(Exeggcute, self).draw()
        pass

    def handle_event(self, event):
        super(Exeggcute, self).handle_event(event)
        pass