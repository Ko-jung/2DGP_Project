#웅크리기

from Skill.skill import *

class Dndzmflrl(Skill):
    def __init__(self):
        super(Dndzmflrl, self).__init__()
        self.name = "Dndzmflrl"
        self.pp = 40
        self.maxPp = 40
        self.power = 0
        self.type = [Type_Normal]
        self.hitRate = 100
        self.isContact = False
        # 방어 +1