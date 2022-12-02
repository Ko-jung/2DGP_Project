from Pokemon.pokemon import *
from pico2d import *
from random import *

class Nidoran (Pokemon):
    # TODO: 암/수 구분할거임?
    def __init__(self, XY = [24, 12], level = 5):
        super(Nidoran, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\nidoran.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Poison]

        # 암
        self.BS_Hp   = 55
        self.BS_Atk  = 47
        self.BS_Def  = 52
        self.BS_Sp_A = 40
        self.BS_Sp_D = 40
        self.BS_Spd  = 41

        # 수
        # self.BS_Hp = 46
        # self.BS_Atk = 57
        # self.BS_Def = 40
        # self.BS_Sp_A = 40
        # self.BS_Sp_D = 40
        # self.BS_Spd = 50
        super(Nidoran, self).setValue()

        pass

    def update(self):
        super(Nidoran, self).update()
        pass

    def draw(self):
        super(Nidoran, self).draw()
        pass

    def handle_event(self, event):
        super(Nidoran, self).handle_event(event)
        pass