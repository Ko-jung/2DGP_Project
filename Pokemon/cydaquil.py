from Pokemon.pokemon import *
from pico2d import *
from random import *

class Cydaquil (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Cydaquil, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\cydaquil.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Fire]

        self.BS_Hp   = 39
        self.BS_Atk  = 52
        self.BS_Def  = 43
        self.BS_Sp_A = 60
        self.BS_Sp_D = 50
        self.BS_Spd  = 65
        super(Cydaquil, self).setValue()

        pass

    def update(self):
        super(Cydaquil, self).update()
        pass

    def draw(self):
        super(Cydaquil, self).draw()
        # TODO: 불꽃 이미지도 따로 그려줘야함
        pass

    def handle_event(self, event):
        super(Cydaquil, self).handle_event(event)
        pass