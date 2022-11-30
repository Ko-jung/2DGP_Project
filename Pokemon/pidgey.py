from Pokemon.aipokemon import AiPokemon
from Pokemon.pokemon import *
from pico2d import *
from random import *

class Pidgey (AiPokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Pidgey, self).__init__()
        self.x, self.y = XY[0], XY[1]
        print(f'Pidgey {self.x, self.y = }')
        self.image = load_image('Pokemon\\Image\\pidgey.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Normal, Type_Flying]

        self.BS_Hp   = 40
        self.BS_Atk  = 45
        self.BS_Def  = 40
        self.BS_Sp_A = 35
        self.BS_Sp_D = 35
        self.BS_Spd  = 56

        super(Pidgey, self).setValue()

        pass

    def update(self):
        super(Pidgey, self).update()
        pass

    def draw(self):
        super(Pidgey, self).draw()
        pass

    def handle_event(self, event):
        super(Pidgey, self).handle_event(event)
        pass