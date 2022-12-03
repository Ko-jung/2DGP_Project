from Pokemon.pokemon import *
from pico2d import *
from random import *

class Chikorita (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Chikorita, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\chikorita.png')
        self.fullFrame = 2

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Grass]

        self.BS_Hp   = 45
        self.BS_Atk  = 49
        self.BS_Def  = 65
        self.BS_Sp_A = 49
        self.BS_Sp_D = 65
        self.BS_Spd  = 45
        super(Chikorita, self).setValue()

        pass

    def update(self):
        super(Chikorita, self).update()
        pass

    def draw(self):
        super(Chikorita, self).draw()
        pass

    def handle_event(self, event):
        super(Chikorita, self).handle_event(event)
        pass