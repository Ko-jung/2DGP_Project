from Pokemon.pokemon import *
from Pokemon.aipokemon import *
from pico2d import *
from random import *

class Magnemite (AiPokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Magnemite, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\magnemite.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Elect, Type_Steel]

        self.BS_Hp   = 25
        self.BS_Atk  = 35
        self.BS_Def  = 70
        self.BS_Sp_A = 95
        self.BS_Sp_D = 55
        self.BS_Spd  = 45
        super(Magnemite, self).setValue()

        pass

    def update(self):
        super(Magnemite, self).update()
        pass

    def draw(self):
        super(Magnemite, self).draw()
        pass

    def handle_event(self, event):
        super(Magnemite, self).handle_event(event)
        pass