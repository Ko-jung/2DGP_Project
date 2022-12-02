from Pokemon.pokemon import *
from pico2d import *
from random import *

class Mudkip (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Mudkip, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\mudkip.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Water]

        self.BS_Hp   = 50
        self.BS_Atk  = 70
        self.BS_Def  = 50
        self.BS_Sp_A = 50
        self.BS_Sp_D = 50
        self.BS_Spd  = 40
        super(Mudkip, self).setValue()

        pass

    def update(self):
        super(Mudkip, self).update()
        pass

    def draw(self):
        super(Mudkip, self).draw()
        pass

    def handle_event(self, event):
        super(Mudkip, self).handle_event(event)
        pass