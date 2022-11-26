#매그니튜드
from Skill.skill import *
import random

class Aormslxbem(Skill):
    def __init__(self):
        super(Aormslxbem, self).__init__()
        self.name = "Aormslxbem"
        self.pp = 30
        self.maxPp = 30
        self.power = None
        self.type = [Type_Rock]
        self.hitRate = 100
        self.isContact = True
        # 4~10 규모에 위력 10 30 50 ... 150까지 증가 확률은 5 10 20 30 20 10 5