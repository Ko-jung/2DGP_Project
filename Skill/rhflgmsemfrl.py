from Skill.skill import *

class Rhflgmsemfrl(Skill):
    def __init__(self):
        super(Rhflgmsemfrl, self).__init__()
        # self.name = "Rflgmsemfrl"
        self.name = "꼬리흔들기"
        self.power = 0
        self.type = [Type_Normal]
        self.pp = 30
        self.maxPp = 30
        self.hitRate = 100
        self.isContact = False
        # 100확률로 대상의 방어 -1


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
        deffencer.getDebuff()
        Skill.debuffSound.play(1)
        pass