#볼트태클
from Skill.skill import *

class Qhfxmxozmf(Skill):
    def __init__(self):
        super(Qhfxmxozmf, self).__init__()
        self.name = "Qhfxmxozmf"
        self.pp = 15
        self.maxPp = 15
        self.power = 120
        self.type = [Type_Elect]
        self.hitRate = 100
        self.isContact = True
        # 준 피해의 1/3을 자신도 입음

    def useSkill(self, attacker, deffencer):
        damage = super(Qhfxmxozmf, self).calculationDamage(attacker, deffencer)
        deffencer.getDamage(damage)
        attacker.getDamage(damage//3)
        pass