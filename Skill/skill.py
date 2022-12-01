import game_world
import random

Type_Normal, Type_Fire, Type_Water, Type_Elect, Type_Grass, Type_Ice, Type_Fight, Type_Poison, Type_Ground, Type_Flying,\
Type_Psy, Type_Bug, Type_Rock, Type_Ghost, Type_Dragon, Type_Dark, Type_Steel = range(17)

# typeCounter[other][main]
typeCounter = [\
#    N,     F,     W,     E,     G,     I,     F,     P,     G,   Fly,   Psy,      B,     Rock, Ghost,   D,  Dark,     S
    [1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,      1,      0.5,   0,     1,     1,     1],   # N
    [1,   0.5,   0.5,     1,     2,     2,     1,     1,     1,     1,     1,      2,      0.5,   1,   0.5,     1,     2],   # F
    [1,     2,   0.5,     1,   0.5,     1,     1,     1,     2,     1,     1,      1,      2,     1,   0.5,     1,     1],   # W
    [1,     1,     2,   0.5,   0.5,     1,     1,     1,     0,     2,     1,      1,      1,     1,   0.5,     1,     1],   # E
    [1,   0.5,     2,     1,   0.5,     1,     1,   0.5,     2,   0.5,     1,    0.5,      2,     1,   0.5,     1,   0.5],   # G
    [1,   0.5,   0.5,     1,     2,   0.5,     1,     1,     2,     2,     1,      1,      1,     1,     2,     1,   0.5],   # I
    [2,     1,     1,     1,     1,     2,     1,   0.5,     1,   0.5,   0.5,    0.5,      2,     0,     1,     2,     2],   # F
    [1,     1,     1,     1,     2,     1,     1,   0.5,   0.5,     1,     1,      1,    0.5,   0.5,     1,     1,     0],   # P
    [1,     2,     1,     2,   0.5,     1,     1,     2,     1,     0,     1,    0.5,      2,     1,     1,     1,     2],   # G
    [1,     1,     1,   0.5,     2,     1,     2,     1,     1,     1,     1,      2,    0.5,     1,     1,     1,   0.5],   # Fly
    [1,     1,     1,     1,     1,     1,     2,     2,     1,     1,   0.5,      1,      1,     1,     1,     0,   0.5],   # Psy
    [1,   0.5,     1,     1,     2,     1,   0.5,   0.5,     1,   0.5,     2,      1,      1,   0.5,     1,     2,   0.5],   # B
    [1,     2,     1,     1,     1,     2,   0.5,     1,   0.5,     2,     1,      2,      1,     1,     1,     1,   0.5],   # Rock
    [0,     1,     1,     1,     1,     1,     1,     1,     1,     1,     2,      1,      1,     2,     1,   0.5,   0.5],   # Ghost
    [1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,      1,      1,     1,     2,     1,   0.5],   # D
    [1,     1,     1,     1,     1,     1,   0.5,     1,     1,     1,     2,      1,      1,     2,     1,   0.5,   0.5],   # Dark
    [1,   0.5,   0.5,   0.5,     1,     2,     1,     1,     1,     1,     1,      1,      2,     1,     1,     1,   0.5] ] # S

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
    def isSelfBuff(self):
        print("isSelfBuff")
        return False

    def useSkill(self, attacker, deffencer):
        damage = self.calculationDamage(attacker, deffencer)
        deffencer.getDamage(int(damage))
        pass
    def calculationDamage(self, attacker, deffencer):
        # (데미지 = (((((((레벨 × 2 ÷ 5) + 2) × 위력 × 특수공격 ÷ 50) ÷ 특수방어) × Mod1) + 2) × [[급소]] × Mod2) × 자속보정 × 타입상성1 × 타입상성2 × 랜덤수 ÷ 100)

        # 급소 공격 확률 15%
        if random.randint(1,100) <= 15: critical = 2
        else: critical = 1

        # 자속기
        sameType = 1
        for t in attacker.Type:
            if t == self.type:
                sameType = 1.5
                break

        # 상성 공격
        typeDamage = [1, 1]
        typeCount = 0
        for t in deffencer.Type:
            typeDamage[typeCount] = typeCounter[t][self.type[0]]
            typeCount += 1

        damage = (((((((attacker.Level * 2 / 5) + 2) * self.power * attacker.Atk / 50) / deffencer.Def) + 2) * critical) * sameType * typeDamage[0] * typeDamage[1] * (random.randint(85,100) / 100) / 100)
        return damage


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

    def findNearOther(self, mainchar):
        x, y = mainchar.x, mainchar.y
        map = game_world.objects[game_world.BACKOBJECT][0]
        enemylist = map.enemyList[map.floor]
        otherList = []
        for e in enemylist:
            if x - 3 <= e.x <= x + 3 and y - 3 <= e.y <= y + 3:
                otherList.append(e)
        return otherList
        pass