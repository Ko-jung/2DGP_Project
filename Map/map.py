from pico2d import *
import random
import game_world
from game_world import *
import server
import game_framework
# from Pokemon.pokemon import Pokemon

from Pokemon.pidgey import Pidgey
from Pokemon.sunkern import Sunkern
from Pokemon.wurmple import Wurmple
from Pokemon.exeggcute import Exeggcute

from Pokemon.aron import Aron
from Pokemon.zigzagoon import Zigzagoon
from Pokemon.geodude import Geodude

from Pokemon.magnemite import Magnemite
from Pokemon.rattata import Rattata
from Pokemon.nidoran import Nidoran
from Pokemon.poochyena import Poochyena
from Pokemon.voltorb import Voltorb
from Pokemon.minun import Minun
from Pokemon.plusle import Plusle


import logo_state
import square_state
class Map:
    def __init__(self, imageArray = None, timage = None, floor = 0, randomPos = None, mapName = None):
        self.tileImage = timage
        self.imageArr = imageArray
        self.floor = floor
        self.startPos = randomPos
        self.mapName = mapName
        self.font = load_font('Font\\tvN 즐거운이야기 Medium.TTF', 240)
        self.blackpic = load_image('BlackPic.png')
        self.timer = 0.0
        self.alpha = 0.0

        self.enemyList = [[] for c in imageArray]
        if mapName == 'TinyForest':
            self.spawnTinyEnemy()
        else:
            self.spawnSteelEnemy()
        game_world.add_objects(self.enemyList[self.floor], AIOBJECT)
        # print(self.enemyList)

    def getEnemyList(self, floor):
        return self.enemyList[floor]

    def isOverMap(self, poke):
        nowPosTile = self.imageArr[self.floor][24 - ((int)(poke.nextY))][((int)(poke.nextX))]
        if not 16 <= nowPosTile <= 22 :
            print(f'{poke} is over map {nowPosTile = }, {poke.nextX, poke.nextY = }')
            return True
        return False

    def update(self):
        if server.changeState:
            return
        nowPosTile = self.imageArr[self.floor][(int)(24 - objects[MAINOBJECT][0].y)][(int)(objects[MAINOBJECT][0].x)]
        if nowPosTile == 22 and objects[MAINOBJECT][0].x == int(objects[MAINOBJECT][0].x) and objects[MAINOBJECT][0].y == int(objects[MAINOBJECT][0].y):
            if self.floor < len(self.imageArr) - 1:
                print('update', self.enemyList[self.floor], self.floor)
                for i in range(len(self.enemyList[self.floor])):
                    game_world.remove_object(self.enemyList[self.floor][i])
                self.floor += 1
                game_world.add_objects(self.enemyList[self.floor], AIOBJECT)
                # print(f'{self.startPos[self.floor] = }')
                objects[MAINOBJECT][0].moveToPos(self.startPos[self.floor][random.randint(0, len(self.startPos[self.floor]) - 1)])
            elif self.floor == len(self.imageArr) - 1:
                server.changeState = True
            pass
        pass

    def draw(self):
        if server.changeState:
            return
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

    def spawnTinyEnemy(self):
        for i in range(len(self.imageArr)):
            for j in range(random.randint(4, 7)):
                temp = random.randint(0, len(self.startPos[i]) - 1)
                match random.randint(0, 3):
                    case 0:
                        self.enemyList[i].append(Pidgey(self.startPos[i][temp]))
                        # print(f'Pidgey {i, j, temp} , {randomPos[i][tem p]}')
                    case 1:
                        self.enemyList[i].append(Sunkern(self.startPos[i][temp]))
                        # print(f'Sunkern {i, j, temp} , {randomPos[i][temp]}')
                    case 2:
                        self.enemyList[i].append(Wurmple(self.startPos[i][temp]))
                        # print(f'Wurmple {i, j, temp} , {randomPos[i][temp]}')
                    case 3:
                        self.enemyList[i].append(Exeggcute(self.startPos[i][temp]))
                    # print(f'Exeggcute {i, j, temp} , {randomPos[i][temp]}')
        # print(r"===========")

    def spawnSteelEnemy(self):
        for i in range(4):
            for j in range(random.randint(4, 7)):
                temp = random.randint(0, len(self.startPos[i]) - 1)
                match random.randint(0, 4):
                    case 0:
                        self.enemyList[i].append(Aron(self.startPos[i][temp], random.randint(5,12)))
                    case 1:
                        self.enemyList[i].append(Zigzagoon(self.startPos[i][temp], random.randint(5,12)))
                    case 2:
                        self.enemyList[i].append(Geodude(self.startPos[i][temp], random.randint(5,12)))
                    case 3:
                        self.enemyList[i].append(Poochyena(self.startPos[i][temp], random.randint(5,12)))
                    case 4:
                        self.enemyList[i].append(Rattata(self.startPos[i][temp], random.randint(5,12)))
        for i in range(4, 9):
            for j in range(random.randint(4, 7)):
                temp = random.randint(0, len(self.startPos[i]) - 1)
                match random.randint(0, 6):
                    case 0:
                        self.enemyList[i].append(Magnemite(self.startPos[i][temp], random.randint(15,25)))
                    case 1:
                        self.enemyList[i].append(Nidoran(self.startPos[i][temp], random.randint(15,25)))
                    case 3:
                        self.enemyList[i].append(Voltorb(self.startPos[i][temp], random.randint(15,25)))
                    case 4:
                        self.enemyList[i].append(Minun(self.startPos[i][temp], random.randint(15,25)))
                    case 5:
                        self.enemyList[i].append(Plusle(self.startPos[i][temp], random.randint(15,25)))