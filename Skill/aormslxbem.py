#매그니튜드
from Skill.skill import *
import random

class Aormslxbem(Skill):
    def __init__(self):
        super(Aormslxbem, self).__init__()
        self.name = "매그니튜드"
        # self.name = "Aormslxbem"
        self.pp = 30
        self.maxPp = 30
        self.power = None
        self.type = [Type_Rock]
        self.hitRate = 100
        self.isContact = True
        # 4~10 규모에 위력 10 30 50 ... 150까지 증가 확률은 5 10 20 30 20 10 5

    def useSkill(self, attacker, deffencer):
        rInt = random.randint(1, 100)
        if 1 <= rInt < 5 : self.power = 30
        elif 5 <= rInt < 15 : self.power = 50
        elif 15 <= rInt < 35 : self.power = 70
        elif 35 <= rInt < 65 : self.power = 90
        elif 65 <= rInt < 85 : self.power = 110
        elif 85 <= rInt < 95 : self.power = 130
        elif 95 <= rInt <= 100 : self.power = 150
        super(Aormslxbem, self).useSkill(attacker, deffencer)
        pass