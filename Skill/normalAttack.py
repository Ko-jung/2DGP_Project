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
        if Skill.normalSound is None:
            Skill.criticalSound = load_wav('Sound\\CriticalAttack.wav')
            Skill.criticalSound.set_volume(32)
            Skill.normalSound = load_wav('Sound\\NormalAttack.wav')
            Skill.normalSound.set_volume(32)
            Skill.debuffSound = load_wav('Sound\\Debuff.wav')
            Skill.debuffSound.set_volume(32)
            Skill.buffSound = load_wav('Sound\\Shiled.wav')
            Skill.buffSound.set_volume(32)
        # 급소 공격 확률 15%
        if random.randint(1,100) <= 15:
            critical = 2
            Skill.criticalSound.play(1)
        else:
            critical = 1
            Skill.normalSound.play(1)

        damage = (((((((attacker.Level * 2 / 5) + 2) * self.power * attacker.Atk / 50) / deffencer.Def) + 2) * critical) * 1 * (random.randint(85,100)) / 100)

        print(f'{deffencer.isHit = }')
        if not deffencer.isHit:
            deffencer.getDamage(int(damage))
        print(f'NormalAttack {damage = }')
        pass