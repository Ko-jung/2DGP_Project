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



    def useSkill(self, attacker, deffencer):
        # 급소 공격 확률 15%
        if random.randint(0, 100) <= 15:
            critical = 2
        else:
            critical = 1

        damage = (((((((attacker.Level * 2 / 5) + 2) * self.power * attacker.Atk / 50) / deffencer.Def) + 2) * critical) * 1 * (random.randint(85,100)) / 100)

        deffencer.getDamage(int(damage))
        print(f'NormalAttack {damage = }')
        pass