# 염동력

from Skill.skill import *

class Duaehdfur(Skill):
    def __init__(self):
        super(Duaehdfur, self).__init__()
        self.name = "Duaehdfur"
        self.pp = 25
        self.maxPp = 25
        self.power = 50
        self.type = [Type_Normal]
        self.hitRate = 100
        self.isContact = False