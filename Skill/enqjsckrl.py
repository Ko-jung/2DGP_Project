#두번 차기

from Skill.skill import *


class Enqjsckrl(Skill):
    def __init__(self):
        super(Enqjsckrl, self).__init__()
        self.name = "Enqjsckrl"
        self.type = [Type_Fight]
        self.pp = 30
        self.maxPp = 30
        self.power = 30
        self.hitRate = 100
        self.isContact = True

    def useSkill(self, other):
        pass
