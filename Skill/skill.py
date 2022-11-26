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

    def findFrontOther(self, mainchar):
        x, y = mainchar.x, mainchar.y
        map = game_world.objects[game_world.BACKOBJECT][0]
        eList = map.enemyList[map.floor]
        if mainchar.dir == game_world.DIR_NE:   x, y = x + 1, y + 1
        elif mainchar.dir == game_world.DIR_E:  x, y = x + 1, y
        elif mainchar.dir == game_world.DIR_SE: x, y = x + 1, y - 1
        elif mainchar.dir == game_world.DIR_N:  x, y = x,     y + 1
        elif mainchar.dir == game_world.DIR_NW: x, y = x - 1, y + 1
        elif mainchar.dir == game_world.DIR_W:  x, y = x - 1, y
        elif mainchar.dir == game_world.DIR_SW: x, y = x - 1, y - 1
        elif mainchar.dir == game_world.DIR_S:  x, y = x,     y - 1

        for e in eList:
            if e.x == x and e.y == y:
                return e
        return None
        pass

    def findNearOther(self, mainchar, map):
        x, y = mainchar.x, mainchar.y
        enemylist = map.enemyList[map.floor]
        for e in enemylist:
            if x - 3 <= e.x <= x + 3 and y - 3 <= e.y <= y + 3:
                yield e
        pass