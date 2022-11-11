from pico2d import *
import random

import game_world
from game_world import *
from Pokemon.pokemon import *

from Pokemon.pidgey import Pidgey
from Pokemon.sunkern import Sunkern
from Pokemon.wurmple import Wurmple
from Pokemon.exeggcute import Exeggcute
class Map:
    def __init__(self, imageArray = None, timage = None, floor = 0, randomPos = None):
        self.tileImage = timage
        self.imageArr = imageArray
        self.floor = floor
        self.startPos = randomPos

        self.enemyList = [[] for c in imageArray]
        for i in range(len(imageArray)):
            for j in range(5):

                match random.randint(0, 4):
                    case 0:
                        self.enemyList[i].append(Pidgey(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]))
                    case 1:
                        self.enemyList[i].append(Sunkern(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]))
                    case 2:
                        self.enemyList[i].append(Wurmple(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]))
                    case 3:
                        self.enemyList[i].append(Exeggcute(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]))

        for i in self.enemyList[0]:
            print(i.x, i.y)
        #game_world.add_objects(self.enemyList[self.floor], AIOBJECT)

    def isOverMap(self, poke):
        nowPosTile = self.imageArr[self.floor][24 - (int)(poke.y)][(int)(poke.x)]
        if not 16 <= nowPosTile <= 22 :
            return True
            pass
        pass

    def update(self):
        nowPosTile = self.imageArr[self.floor][(int)(24 - objects[MAINOBJECT][0].y)][(int)(objects[MAINOBJECT][0].x)]
        if nowPosTile == 22:
            if self.floor < len(self.imageArr) - 1:
                self.floor += 1
                objects[MAINOBJECT][0].moveToPos(self.startPos[self.floor][random.randint(0, len(self.startPos[self.floor]))])
            pass
        pass

    def draw(self):
        # print(f'aaaaaa{objects[MAINOBJECT][0].x - printImageX - 1}, {objects[MAINOBJECT][0].y - printImageY - 1}')
        for i in range((int)(objects[MAINOBJECT][0].x - printImageX - 1), (int)(objects[MAINOBJECT][0].x + printImageX + 2)):
            for j in range((int)(objects[MAINOBJECT][0].y - printImageY - 1), (int)(objects[MAINOBJECT][0].y + printImageY + 2)):
                if 0 <= i < 48 and 0 <= j < 25:
                    self.tileImage.clip_draw(24 * (self.imageArr[self.floor][24 - j][i] % 8), 24 * (self.imageArr[self.floor][24 - j][i] // 8), 24, 24,
                                     (i - objects[MAINOBJECT][0].x + printImageX) * 28 * printSize + 14 * printSize,
                                     (j - objects[MAINOBJECT][0].y + printImageY + 1) * 28 * printSize - 14 * printSize,
                                     28 * printSize, 28 * printSize)
                else:
                    self.tileImage.clip_draw(24 * (23 % 8), 24 * (23 // 8), 24, 24,
                                     (i - objects[MAINOBJECT][0].x + printImageX) * 28 * printSize + 14 * printSize,
                                     (j - objects[MAINOBJECT][0].y + printImageY + 1) * 28 * printSize - 14 * printSize,
                                     28 * printSize, 28 * printSize)

                    # for i in range(48):
                    #     for j in range(25):
                    #         timage.clip_draw(24 * (imageArray[24 - j][i] % 8), 24 * (imageArray[24 - j][i] // 8), 24, 24, i * 28, j * 28, 28, 28)
        # TODO: 나중에 지워라
        pass

    def handle_event(self, event):
        pass