import game_world

Type_Normal, Type_Fire, Type_Water, Type_Elect, Type_Grass, Type_Ice, Type_Fight, Type_Poison, Type_Ground, Type_Flying,\
Type_Psy, Type_Bug, Type_Rock, Type_Ghost, Type_Dragon, Type_Dark, Type_Steel = range(17)

# TODO: 스킬의 부가 효과 구현
class Skill:
    def __init__(self):
        self.name = ""
        self.type = []
        self.power = None
        self.pp = None
        self.maxPp = None
        self.hitRate = None
        self.isContact = None

    def useSkill(self, other):
        pass

    def findFrontOther(self, direction):

        pass

    def findNearOther(self):
        pass