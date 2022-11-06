from Pokemon.pokemon import *
from pico2d import *
from random import *

class Geodude (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Geodude, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\geodude.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Ground, Type_Rock]

        self.BS_Hp   = 40
        self.BS_Atk  = 80
        self.BS_Def  = 100
        self.BS_Sp_A = 30
        self.BS_Sp_D = 30
        self.BS_Spd  = 20

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
        super(Geodude, self).update()
        pass

    def draw(self):
        super(Geodude, self).draw()
        pass

    def handle_event(self, event):
        super(Geodude, self).handle_event(event)
        pass