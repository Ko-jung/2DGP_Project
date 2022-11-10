from Pokemon.pokemon import *
from pico2d import *
from random import *


class Zapdos (Pokemon):
    def __init__(self, XY=[24, 12], level=5):
        super(Zapdos, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\zapdos.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Elect, Type_Flying]

        self.BS_Hp = 90
        self.BS_Atk = 90
        self.BS_Def = 85
        self.BS_Sp_A = 125
        self.BS_Sp_D = 90
        self.BS_Spd = 100

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
        super(Zapdos, self).update()
        pass

    def draw(self):
        super(Zapdos, self).draw()
        pass

    def handle_event(self, event):
        super(Zapdos, self).handle_event(event)
        pass