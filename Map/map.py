from pico2d import *
import random
from game_world import *
from Pokemon.pokemon import *

class Map:
    def __init__(self, imageArray = None, timage = None, floor = 0, randomPos = None):
        self.tileImage = timage
        self.imageArr = imageArray
        self.floor = floor
        self.startPos = randomPos

    def isOverMap(self, poke):
        nowPosTile = self.imageArr[self.floor][24 - poke.y][poke.x]
        if not 16 <= nowPosTile <= 22 :
            return True
            pass
        pass

    def update(self):
        nowPosTile = self.imageArr[self.floor][24 - objects[MAINOBJECT][0].y][objects[MAINOBJECT][0].x]
        if nowPosTile == 22:
            if self.floor < len(self.imageArr) - 1:
                self.floor += 1
                objects[MAINOBJECT][0].moveToPos(self.startPos[self.floor][random.randint(0, len(self.startPos[self.floor]))])
            pass
        pass

    def draw(self):
        for i in range(objects[MAINOBJECT][0].x - printImageX - 1, objects[MAINOBJECT][0].x + printImageX + 2):
            for j in range(objects[MAINOBJECT][0].y - printImageY - 1, objects[MAINOBJECT][0].y + printImageY + 2):
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