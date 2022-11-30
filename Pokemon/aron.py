from Pokemon.pokemon import *
from pico2d import *

class Aron (Pokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Aron, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\aron.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Steel, Type_Rock]

        self.BS_Hp   = 50
        self.BS_Atk  = 70
        self.BS_Def  = 100
        self.BS_Sp_A = 40
        self.BS_Sp_D = 40
        self.BS_Spd  = 30

        super(Aron, self).setValue()
        pass

    def update(self):
        super(Aron, self).update()
        pass

    def draw(self):
        super(Aron, self).draw()
        pass

    def handle_event(self, event):
        super(Aron, self).handle_event(event)
        pass