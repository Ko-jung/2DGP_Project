from Pokemon.pokemon import *
from pico2d import *
from random import *


class Weedle (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Weedle, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\weedle.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Bug, Type_Poison]

        self.BS_Hp = 40
        self.BS_Atk = 35
        self.BS_Def = 30
        self.BS_Sp_A = 20
        self.BS_Sp_D = 20
        self.BS_Spd = 50

        self.IV_Hp = randint(0, 31)
        self.IV_Atk = randint(0, 31)
        self.IV_Def = randint(0, 31)
        self.IV_Sp_A = randint(0, 31)
        self.IV_Sp_D = randint(0, 31)
        self.IV_Spd = randint(0, 31)

        self.Hp = int(((self.BS_Hp * 2 + self.IV_Hp + 100) / self.Level * 100) + 5)
        self.Atk = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Def = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Sp_A = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Sp_D = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)
        self.Spd = int(((self.BS_Hp * 2 + self.IV_Hp) / self.Level * 100) + 5)

        pass

    def update(self):
        super(Weedle, self).update()
        pass

    def draw(self):
        super(Weedle, self).draw()
        pass

    def handle_event(self, event):
        super(Weedle, self).handle_event(event)
        pass