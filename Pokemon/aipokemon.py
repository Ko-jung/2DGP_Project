from pico2d import *
from game_world import *
import game_framework
from Pokemon.pokemon import *
from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf

import random
import math


class AiPokemon(Pokemon):
    def __init__(self):
        super(AiPokemon, self).__init__()
        self.isDead = False
        self.isHit = False
        self.u = 0.0
        self.build_behavior_tree()

    def update(self):
        if self.isHit:
            self.u += game_framework.frame_time
            if self.u > 2.0:
                if self.isDead:
                    map = objects[BACKOBJECT][0]
                    eList = map.enemyList[map.floor]
                    for o in eList:
                        if o == self:
                            eList.remove(o)
                            print(eList)
                            break
                    remove_object(self)
                self.u = 0.0
                self.isHit = False
                self.image.opacify(1)
        else:
            self.bt.run()
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame

        if self.drawDebuff:
            self.wait = (self.wait + 1)
            if self.wait >= 100:
                self.drawDebuff = False
            elif self.wait % 5 == 0:
                self.effectFrame = (self.effectFrame + 1) % 11
        pass

    def debuffDraw(self, x = 15, y = 9):
        # print('AIpokemon Class debuffDraw')
        Pokemon.effect.clip_draw(104 + self.effectFrame * 16, 352 - 1 - 207,  16, 16, (28 * 3 * (15 + x * 2)) // 2 + 16,
                                 (28 * 3 * (9 + y * 2)) // 2 - 16, 16 * 3, 16 * 3)

    def draw(self):
        # print(f'{self}, {self.x, self.y = }')
        x = (self.x - objects[MAINOBJECT][0].x)
        y = (self.y - objects[MAINOBJECT][0].y)
        if - printImageX - 1 <= x <= printImageX + 1 and - printImageY - 1 <= y <= printImageY + 1:
            self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * (15 + x * 2)) // 2,
                                 (28 * 3 * (9 + y * 2)) // 2, 28 * 3, 28 * 3)
            if self.isHit:
                if int(self.u / 0.5) % 2 == 0:
                    self.image.opacify(1)
                else:
                    self.image.opacify(0.5)
            pass
        # self.font.draw((28 * 3 * (15 + x * 2)) // 2, (28 * 3 * (9 + y * 2)) // 2, f'(x, y): {self.x:.2f}, {self.y:.2f})', (0, 0, 0))
        if self.drawDebuff:
            self.debuffDraw(x, y)
        pass

    def handle_event(self, event):
        pass

    def moveToPos(self, XY):
        pass

    def overMap(self, x=0, y=0):
        pass

    def getDamage(self, damage):
        self.Hp -= damage
        self.frame = 8
        self.isHit = True
        print(f'getDamage: {self = }, {self.Hp = }')
        self.Hp = clamp(0, self.Hp, self.MaxHp)
        if self.Hp == 0:
            print(f'isDead')
            self.isDead = True
        pass

    def find_random_location(self):
        canGoList = ['STAY']
        map = objects[BACKOBJECT][0].imageArr[objects[BACKOBJECT][0].floor]
        if 16 <= map[24 - int(self.y + 1)][int(self.x + 1)] <= 22: canGoList.append([DIR_NE, int(self.x + 1), int(self.y + 1)])
        if 16 <= map[24 - int(self.y    )][int(self.x + 1)] <= 22: canGoList.append([DIR_E,  int(self.x + 1), int(self.y    )])
        if 16 <= map[24 - int(self.y - 1)][int(self.x + 1)] <= 22: canGoList.append([DIR_SE, int(self.x + 1), int(self.y - 1)])
        if 16 <= map[24 - int(self.y + 1)][int(self.x    )] <= 22: canGoList.append([DIR_N,  int(self.x    ), int(self.y + 1)])
        if 16 <= map[24 - int(self.y - 1)][int(self.x    )] <= 22: canGoList.append([DIR_S,  int(self.x    ), int(self.y - 1)])
        if 16 <= map[24 - int(self.y + 1)][int(self.x - 1)] <= 22: canGoList.append([DIR_NW, int(self.x - 1), int(self.y + 1)])
        if 16 <= map[24 - int(self.y    )][int(self.x - 1)] <= 22: canGoList.append([DIR_W,  int(self.x - 1), int(self.y    )])
        if 16 <= map[24 - int(self.y - 1)][int(self.x - 1)] <= 22: canGoList.append([DIR_SW, int(self.x - 1), int(self.y - 1)])

        if random.randint(0, 9) <= 6:
            rInt = 0
        else:
            rInt = random.randint(1, len(canGoList) - 1)
        # print(rInt, canGoList)
        if canGoList[rInt] != 'STAY' and canGoList[rInt][1] != objects[MAINOBJECT][0].x and canGoList[rInt][2] != objects[MAINOBJECT][0].y:
            self.dir = canGoList[rInt][0]
            self.nextX = canGoList[rInt][1]
            self.nextY = canGoList[rInt][2]
            self.tempX, self.tempY = self.x, self.y
        else:
            self.nextX, self.nextY = self.x, self.y
            self.tempX, self.tempY = self.x, self.y

        return BehaviorTree.SUCCESS

    def move_to(self):
        self.u += 0.05
        if self.u > 1.0:
            self.x = (int)(self.nextX)
            self.y = (int)(self.nextY)
            self.u = 0.0
            return BehaviorTree.SUCCESS
        else:
            self.x = (1 - self.u) * self.tempX + self.u * self.nextX
            self.y = (1 - self.u) * self.tempY + self.u * self.nextY
            return BehaviorTree.RUNNING

    def find_main(self):
        # print('ENTER find_main')
        detectRange = 4
        if -detectRange <= self.x - objects[MAINOBJECT][0].x <= detectRange and -detectRange <= self.y - objects[MAINOBJECT][0].y <= detectRange:
            # print('find_main BehaviorTree.SUCCESS')
            return BehaviorTree.SUCCESS
        else:
            # print('find_main BehaviorTree.FAIL')
            return BehaviorTree.FAIL

    def find_main_to_attack(self):
        # print('ENTER find_main_to_attack')
        # if -1 <= self.x - objects[MAINOBJECT][0].x <= 1 and -1 <= self.y - objects[MAINOBJECT][0].y <= 1:
        if -1 <= objects[MAINOBJECT][0].x - self.x <= 1 and -1 <= objects[MAINOBJECT][0].y - self.y <= 1:
            x, y = self.x - objects[MAINOBJECT][0].x, self.y - objects[MAINOBJECT][0].y
            if x >=  1 and y >=  1: self.dir = DIR_SW
            elif x >=  1 and y ==  0: self.dir = DIR_W
            elif x >=  1 and y <= -1: self.dir = DIR_NW
            elif x ==  0 and y >=  1: self.dir = DIR_S
            elif x ==  0 and y <= -1: self.dir = DIR_N
            elif x <= -1 and y >=  1: self.dir = DIR_SE
            elif x <= -1 and y ==  0: self.dir = DIR_E
            elif x <= -1 and y <= -1: self.dir = DIR_NE
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def attack_main(self):
       skillList = []
       for i in range(len(self.skill)):
           if self.skill[i] != None: skillList.append(i)
       rInt =  random.randint(0, len(skillList) - 1)
       self.currSkillIndex = rInt
       if self.skill[rInt] != None:
           if self.skill[self.currSkillIndex].isContact:
               print('useSkioll')
               if   self.dir == DIR_NE: self.nextX, self.nextY = 15 + 2, 9 + 2
               elif self.dir == DIR_E: self.nextX, self.nextY = 15 + 2, 9
               elif self.dir == DIR_SE: self.nextX, self.nextY = 15 + 2, 9 - 2
               elif self.dir == DIR_N: self.nextX, self.nextY = 15, 9 + 2
               elif self.dir == DIR_S: self.nextX, self.nextY = 15, 9 - 2
               elif self.dir == DIR_NW: self.nextX, self.nextY = 15 - 2, 9 + 2
               elif self.dir == DIR_W: self.nextX, self.nextY = 15 - 2, 9
               elif self.dir == DIR_SW: self.nextX, self.nextY = 15 - 2, 9 - 2
               self.moveAttack = True
               # 리스트 변수 리턴
               self.targetEnemy = self.skill[self.currSkillIndex].findFrontOther(self)
               self.u = 0.0
               self.wait = 0
               self.moving = False
           else:
               self.moveAttack = False
               if self.skill[self.currSkillIndex].isSelfBuff():
                   self.targetEnemy = [self]
               else:
                   # 리스트 변수 리턴
                   self.targetEnemy = self.skill[self.currSkillIndex].findNearOther(self)
           return BehaviorTree.SUCCESS
       else:
           return BehaviorTree.FAIL

    def attack_do(self):
        if self.moveAttack:
            if self.moving:
                self.u -= 0.1
                if self.u < 0.0: self.add_event(STOP)
                return BehaviorTree.SUCCESS
            else:
                if self.u > 1.0:
                    if not self.targetEnemy is None: self.skill[self.currSkillIndex].useSkill(self, self.targetEnemy)
                    self.moving = True
                else:  self.u += 0.1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame
        else:
            self.wait = (self.wait + 1) % 5
            if self.wait == 0:
                self.u += 0.1
                if 0 <= self.dir <= 2:
                    if self.dir == 2: self.dir = 7
                    else: self.dir += 1
                elif 3 <= self.dir <= 7:
                    if self.dir == 3: self.dir = 0
                    else: self.dir -= 1
                if self.u >= 0.75:
                    for e in self.targetEnemy:
                        self.skill[self.currSkillIndex].useSkill(self, e)
                    self.add_event(STOP)
                    return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    def get_next_pos(self):
        # print('ENTER get_next_pos')
        startX, startY = self.x, self.y
        endX, endY = objects[MAINOBJECT][0].x, objects[MAINOBJECT][0].y
        map = objects[BACKOBJECT][0]
        if endX - startX == 0:
            if endY - startY > 0:
                tempX = startX
                tempY = startY + 1
            else:
                tempX = startX
                tempY = startY - 1
        else:
            # y = divide * x + b
            divide = (endY - startY)/(endX - startX)
            b = startY - divide * startX
            if abs(endX - startX) >= abs(endY - startY):
                if endX- startX < 0: tempX =  startX - 1
                else:                tempX =  startX + 1
                tempY =  round(divide * self.nextX + b)
            else:
                if endY - startY < 0: tempY = startY - 1
                else:                 tempY = startY + 1

                tempX = round((self.nextY - b) / divide)

        if int(tempX) != int(endX) or int(tempY) != int(endY):
            self.nextX, self.nextY = tempX, tempY
            self.tempX, self.tempY = self.x, self.y
        else:
            return BehaviorTree.FAIL

        nowPosTile = map.imageArr[map.floor][24 - ((int)(tempY))][((int)(tempX))]
        if 16 <= nowPosTile <= 22:
            self.nextX, self.nextY = tempX, tempY
            self.tempX, self.tempY = self.x, self.y
        else:
            return BehaviorTree.FAIL

        return BehaviorTree.SUCCESS

    # def move_to_main(self):# TODO: 알아서 길찾아가는 AI 구현 bidirectional 알고리즘?
    #     pass



    def build_behavior_tree(self):
        find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        move_to_node = Leaf('Move To', self.move_to)
        wander_sequence = Sequence('Wander', find_random_location_node, move_to_node)

        # find_main_node = Leaf('Find Main to Move', self.find_main)
        # get_next_pos_node = Leaf('Find Next Pos to Move', self.get_next_pos)
        # find_sequence = Sequence('Find', find_main_node, get_next_pos_node, move_to_node)

        find_main_to_attack_node = Leaf('Find Main to Attack', self.find_main_to_attack)
        attack_main_node = Leaf('Attack Main', self.attack_main)
        attack_do_node = Leaf('Attack do', self.attack_do)
        attack_sequence = Sequence('attack', find_main_to_attack_node, attack_main_node, attack_do_node)

        AIBT = Selector('AI BehaviorTree', attack_sequence, wander_sequence)
        AIBT.print()

        self.bt = BehaviorTree(AIBT)

    # def wander(self):



