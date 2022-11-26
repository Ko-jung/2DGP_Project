#그냥 A키 공격
from Skill.skill import *

class NormalAttack(Skill):
    def __init__(self):
        super(NormalAttack, self).__init__()
        self.name = "NormalAttack"
        self.pp = None
        self.maxPp = None
        self.power = 5
        self.type = None
        self.hitRate = 100
        self.isContact = True



    def useSkill(self, other):

        pass