from Pokemon.pokemon import *
from pico2d import *
from random import *

class Bulbasaur (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Bulbasaur, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\bulbasaur.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Grass, Type_Poison]

        self.BS_Hp   = 45
        self.BS_Atk  = 49
        self.BS_Def  = 49
        self.BS_Sp_A = 65
        self.BS_Sp_D = 65
        self.BS_Spd  = 45
        super(Bulbasaur, self).setValue()

        pass

    def update(self):
        super(Bulbasaur, self).update()
        pass

    def draw(self):
        super(Bulbasaur, self).draw()
        pass

    def handle_event(self, event):
        super(Bulbasaur, self).handle_event(event)
        pass