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

        self.IV_Hp   = randint(0,31)
        self.IV_Atk  = randint(0,31)
        self.IV_Def  = randint(0,31)
        self.IV_Sp_A = randint(0,31)
        self.IV_Sp_D = randint(0,31)
        self.IV_Spd  = randint(0,31)

        self.Hp   = int(((self.BS_Hp * 2 + self.IV_Hp + 100) / self.Level * 100) + 5)
        self.Atk  = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Def  = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Sp_A = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Sp_D = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Spd  = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)

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