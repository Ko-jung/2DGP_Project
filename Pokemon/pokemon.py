from pico2d import *
from game_world import *
import game_framework

Type_Normal, Type_Fire, Type_Water, Type_Elect, Type_Grass, Type_Ice, Type_Fight, Type_Poison, Type_Ground, Type_Flying,\
Type_Psy, Type_Bug, Type_Rock, Type_Ghost, Type_Dragon, Type_Dark, Type_Steel = range(17)

# Pokemon Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

# Pokemon Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Pokemon:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.fullFrame = 3
        self.dir = DIR_S
        self.dirX, self.dirY = 0, 0
        self.image = None
        self.wait = 0

        self.Level = None
        self.Exp = 0
        self.Type = None

        self.Hp   = None
        self.Atk  = None
        self.Def  = None
        self.Sp_A = None
        self.Sp_D = None
        self.Spd  = None

        self.IV_Hp   = None
        self.IV_Atk  = None
        self.IV_Def  = None
        self.IV_Sp_A = None
        self.IV_Sp_D = None
        self.IV_Spd  = None

        self.BS_Hp = None
        self.BS_Atk = None
        self.BS_Def = None
        self.BS_Sp_A = None
        self.BS_Sp_D = None
        self.BS_Spd = None


    def update(self):
        # TODO: 적당한 프레임 움직임 구현
        # TODO: IDLE상태에서 움직임 구현
        self.wait += 1

        if self.dirX > 0 and self.dirY > 0:       self.dir, self.x, self.y = DIR_NE, self.x + 1, self.y + 1
        elif self.dirX > 0 and self.dirY == 0:    self.dir, self.x, self.y = DIR_E , self.x + 1, self.y
        elif self.dirX > 0 and self.dirY < 0:     self.dir, self.x, self.y = DIR_SE, self.x + 1, self.y - 1
        elif self.dirX == 0 and self.dirY > 0:    self.dir, self.x, self.y = DIR_N , self.x, self.y + 1
        elif self.dirX == 0 and self.dirY < 0:    self.dir, self.x, self.y = DIR_S , self.x, self.y - 1
        elif self.dirX < 0 and self.dirY > 0:     self.dir, self.x, self.y = DIR_NW, self.x - 1, self.y + 1
        elif self.dirX < 0 and self.dirY == 0:    self.dir, self.x, self.y = DIR_W , self.x - 1, self.y
        elif self.dirX < 0 and self.dirY < 0:     self.dir, self.x, self.y = DIR_SW, self.x - 1, self.y - 1
        # elif self.dirX == 0 and self.dirY == 0:   self.dir = pokemon.DIR_S

        # if(self.wait % 5 == 0):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame
        self.wait = 0
        pass

    def draw(self):
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2, (28 * 3 * 9) // 2, 28 * 3, 28 * 3)
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == pico2d.SDLK_UP:
                self.dirY += 1
            if event.key == pico2d.SDLK_DOWN:
                self.dirY -= 1
            if event.key == pico2d.SDLK_LEFT:
                self.dirX -= 1
            if event.key == pico2d.SDLK_RIGHT:
                self.dirX += 1
        elif event.type == SDL_KEYUP:
            if event.key == pico2d.SDLK_UP:
                self.dirY -= 1
            if event.key == pico2d.SDLK_DOWN:
                self.dirY += 1
            if event.key == pico2d.SDLK_LEFT:
                self.dirX += 1
            if event.key == pico2d.SDLK_RIGHT:
                self.dirX -= 1
        pass

    def moveToPos(self, XY):
        self.x, self.y = XY[0], XY[1]
        pass

    def overMap(self, x = 0, y = 0):
        if self.dir == DIR_NE:
            self.x += -1
            self.y += -1
        elif self.dir == DIR_E:
            self.x += -1
            self.y +=  0
        elif self.dir == DIR_SE:
            self.x += -1
            self.y +=  1
        elif self.dir == DIR_N:
            self.x +=  0
            self.y += -1
        elif self.dir == DIR_S:
            self.x +=  0
            self.y +=  1
        elif self.dir == DIR_NW:
            self.x +=  1
            self.y += -1
        elif self.dir == DIR_W:
            self.x +=  1
            self.y +=  0
        elif self.dir == DIR_SW:
            self.x +=  1
            self.y +=  1



