from pico2d import *
from game_world import *
import game_framework
from Pokemon.pokemon import Pokemon
import random

from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf

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
        if 16 <= map[24 - (self.y + 1)][self.x + 1] <= 22: canGoList.append([DIR_NE, self.x + 1, self.y + 1])
        if 16 <= map[24 - (self.y    )][self.x + 1] <= 22: canGoList.append([DIR_E, self.x + 1, self.y])
        if 16 <= map[24 - (self.y - 1)][self.x + 1] <= 22: canGoList.append([DIR_SE, self.x + 1, self.y - 1])
        if 16 <= map[24 - (self.y + 1)][self.x    ] <= 22: canGoList.append([DIR_N, self.x, self.y + 1])
        if 16 <= map[24 - (self.y - 1)][self.x    ] <= 22: canGoList.append([DIR_S, self.x, self.y - 1])
        if 16 <= map[24 - (self.y + 1)][self.x - 1] <= 22: canGoList.append([DIR_NW, self.x - 1, self.y + 1])
        if 16 <= map[24 - (self.y    )][self.x - 1]<= 22: canGoList.append([DIR_W, self.x - 1, self.y])
        if 16 <= map[24 - (self.y - 1)][self.x - 1] <= 22: canGoList.append([DIR_SW, self.x - 1, self.y - 1])

        if random.randint(0, 9) <= 6:
            rInt = 0
        else:
            rInt = random.randint(1, len(canGoList) - 1)
        # print(rInt, canGoList)
        if canGoList[rInt] != 'STAY':
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

    def move_to_boy(self):# TODO: 알아서 길찾아가는 AI 구현 bidirectional 알고리즘?
        mainChar = objects[MAINOBJECT][0]
        if -3 <= self.x - mainChar.x <= 3 and -3 <= self.y - mainChar.y <= 3:
            pass
        else:
            return BehaviorTree.FAIL

        if distance > (PIXEL_PER_METER * 10) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        if self.hp > server.boy.hp:
            self.dir = math.atan2(server.boy.y - self.y, server.boy.x - self.x)
            if distance < (PIXEL_PER_METER * 0.5) ** 2:
                self.speed = 0
                return BehaviorTree.SUCCESS
            else:
                self.speed = RUN_SPEED_PPS
                return BehaviorTree.RUNNING
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def build_behavior_tree(self):
        find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        move_to_node = Leaf('Move To', self.move_to)
        wander_sequence = Sequence('Wander', find_random_location_node, move_to_node)
        self.bt = BehaviorTree(wander_sequence)

    # def wander(self):



