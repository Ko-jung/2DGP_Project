from Skill.skill import *

class Ehrcla(Skill):
    def __init__(self):
        super(Ehrcla, self).__init__()
        self.name = "Ehrcla"
        self.pp = 35
        self.maxPp = 35
        self.power = 15
        self.type = [Type_Poison]
        self.hitRate = 100
        self.isContact = True
        # 30퍼 확률로 독