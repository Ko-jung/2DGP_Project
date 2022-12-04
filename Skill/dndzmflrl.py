#웅크리기

from Skill.skill import *

class Dndzmflrl(Skill):
    def __init__(self):
        super(Dndzmflrl, self).__init__()
        self.name = "웅크리기"
        # self.name = "Dndzmflrl"
        self.pp = 40
        self.maxPp = 40
        self.power = 0
        self.type = [Type_Normal]
        self.hitRate = 100
        self.isContact = False
        # 방어 +1

    def isSelfBuff(self):
        if Skill.normalSound is None:
            Skill.criticalSound = load_wav('Sound\\CriticalAttack.wav')
            Skill.criticalSound.set_volume(32)
            Skill.normalSound = load_wav('Sound\\NormalAttack.wav')
            Skill.normalSound.set_volume(32)
            Skill.debuffSound = load_wav('Sound\\Debuff.wav')
            Skill.debuffSound.set_volume(32)
            Skill.buffSound = load_wav('Sound\\Shiled.wav')
            Skill.buffSound.set_volume(32)
        print("isSelfBuff 웅크리기")
        return True
    def useSkill(self, attacker, deffencer):
        print("Use Skill 웅크리기")
        attacker.getBuff('Ammor')
        Skill.buffSound.play(1)
        pass