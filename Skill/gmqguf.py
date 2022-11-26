#흡혈
from Skill.skill import *

class Gmqguf(Skill):
    def __init__(self):
        super(Gmqguf, self).__init__()
        self.name = "Gmqguf"
        self.pp = 15
        self.maxPp = 15
        self.power = 20
        self.type = [Type_Bug]
        self.hitRate = 100
        self.isContact = True
        # 준 피해의 절반만큼 회복