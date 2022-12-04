# 메탈클로
from Skill.skill import *

class Apxkfzmffh(Skill):
    def __init__(self):
        super(Apxkfzmffh, self).__init__()
        # self.name = "Apxkfzmffh"
        self.name = "메탈클로"
        self.type = [Type_Steel]
        self.power = 40
        self.pp = 35
        self.maxPp = 35
        self.hitRate = 100
        self.isContact = True
        # 공격시 10% 확률로 자신의 공격 +1

    def useSkill(self, attacker, deffencer):
        if Skill.normalSound is None:
            Skill.criticalSound = load_wav('Sound\\CriticalAttack.wav')
            Skill.criticalSound.set_volume(32)
            Skill.normalSound = load_wav('Sound\\NormalAttack.wav')
            Skill.normalSound.set_volume(32)
            Skill.debuffSound = load_wav('Sound\\Debuff.wav')
            Skill.debuffSound.set_volume(32)
            Skill.buffSound = load_wav('Sound\\Shiled.wav')
            Skill.buffSound.set_volume(32)
        damage = super(Apxkfzmffh, self).calculationDamage(attacker, deffencer)
        deffencer.getDamage(int(damage))
        if random.randint(0, 9) == 0:
            attacker.getBuff('Attack')
            Skill.buffSound.play(1)
        pass