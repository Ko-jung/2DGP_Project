#구르기
from Skill.skill import *

class Rnfmrl(Skill):
    def __init__(self):
        super(Rnfmrl, self).__init__()
        # self.name = "Rnfmrl"
        self.name = "구르기"
        self.pp = 20
        self.maxPp = 20
        self.power = 30
        self.type = [Type_Rock]
        self.hitRate = 90
        self.isContact = True