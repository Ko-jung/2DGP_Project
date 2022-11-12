from pico2d import *
import random

import game_world
from game_world import *
import game_framework
# from Pokemon.pokemon import Pokemon

from Pokemon.pidgey import Pidgey
from Pokemon.sunkern import Sunkern
from Pokemon.wurmple import Wurmple
from Pokemon.exeggcute import Exeggcute
import square_state
class Map:
    def __init__(self, imageArray = None, timage = None, floor = 0, randomPos = None):
        self.tileImage = timage
        self.imageArr = imageArray
        self.floor = floor
        self.startPos = randomPos

        self.enemyList = [[] for c in imageArray]
        for i in range(len(imageArray)):
            for j in range(random.randint(4, 7)):
                temp = random.randint(0, len(randomPos[i]) - 1)
                match random.randint(0, 3):
                    case 0:
                        self.enemyList[i].append(Pidgey(randomPos[i][temp]))
                        print(f'Pidgey {i, j, temp} , {randomPos[i][temp]}')
                    case 1:
                        self.enemyList[i].append(Sunkern(randomPos[i][temp]))
                        print(f'Sunkern {i, j, temp} , {randomPos[i][temp]}')
                    case 2:
                        self.enemyList[i].append(Wurmple(randomPos[i][temp]))
                        print(f'Wurmple {i, j, temp} , {randomPos[i][temp]}')
                    case 3:
                        self.enemyList[i].append(Exeggcute(randomPos[i][temp]))
                        print(f'Exeggcute {i, j, temp} , {randomPos[i][temp]}')
            print(r"===========")

        game_world.add_objects(self.enemyList[self.floor], AIOBJECT)

    def isOverMap(self, poke):
        nowPosTile = self.imageArr[self.floor][24 - ((int)(poke.nextY))][((int)(poke.nextX))]
        if not 16 <= nowPosTile <= 22 :
            print(f'{poke} is over map {nowPosTile = }, {poke.nextX, poke.nextY = }')
            return True
            pass
        return False
        pass

    def update(self):
        nowPosTile = self.imageArr[self.floor][(int)(24 - objects[MAINOBJECT][0].y)][(int)(objects[MAINOBJECT][0].x)]
        if nowPosTile == 22:
            if self.floor < len(self.imageArr) - 1:
                for i in range(len(self.enemyList[self.floor])):
                    game_world.remove_object(self.enemyList[self.floor][i])

                self.floor += 1
                game_world.add_objects(self.enemyList[self.floor], AIOBJECT)

                objects[MAINOBJECT][0].moveToPos(self.startPos[self.floor][random.randint(0, len(self.startPos[self.floor]))])
            elif self.floor == len(self.imageArr) - 1:
                # TODO: 현재는 그냥 종료하게 했지만 마을로 이동하게 해야함, 그리고 이걸 MAP에서 관리하는게 맞나 싶다
                game_framework.quit()
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
        pass

    def handle_event(self, event):
        pass
