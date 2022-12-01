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

    def isSelfBuff(self):
        print("isSelfBuff 웅크리기")
        return True
    def useSkill(self, attacker, deffencer):
        print("Use Skill 웅크리기")
        attacker.getBuff('Ammor')
        pass