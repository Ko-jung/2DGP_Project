#쪼기
from Skill.skill import *

class Whrl(Skill):
    def __init__(self):
        super(Whrl, self).__init__()
        self.name = "Whrl"
        self.pp = 35
        self.maxPp = 35
        self.power = 35
        self.type = [Type_Flying]
        self.hitRate = 100
        self.isContact = True