from Skill.skill import *

class Rhflgmsemfrl(Skill):
    def __init__(self):
        super(Rhflgmsemfrl, self).__init__()
        self.name = "Rflgmsemfrl"
        self.power = 0
        self.type = [Type_Normal]
        self.pp = 30
        self.maxPp = 30
        self.hitRate = 100
        self.isContact = False
        # 100확률로 대상의 방어 -1