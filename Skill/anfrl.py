from Skill.skill import *

class Anfrl(Skill):
    def __init__(self):
        super(Anfrl, self).__init__()
        self.name = "Anfrl"
        self.type = [Type_Dark]
        self.pp = 25
        self.maxPp = 25
        self.power = 60
        self.hitRate = 100
        self.isContact = True