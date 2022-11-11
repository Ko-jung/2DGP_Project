from pico2d import *
from game_world import *
import game_framework

Type_Normal, Type_Fire, Type_Water, Type_Elect, Type_Grass, Type_Ice, Type_Fight, Type_Poison, Type_Ground, Type_Flying,\
Type_Psy, Type_Bug, Type_Rock, Type_Ghost, Type_Dragon, Type_Dark, Type_Steel = range(17)

#1 : 이벤트 정의
keyCount = 10
RD, LD, RU, LU, UD, UU, DD, DU, STOP, AD = range(keyCount)
event_name = ['RD', 'LD', 'RU', 'LU', 'UD', 'UU', 'DD', 'DU', 'STOP', 'AD']
useKey = [False for _ in range(keyCount)]

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_DOWN): DU,

    (SDL_KEYDOWN, SDLK_a): AD,
}


# Pokemon MOVE Speed
PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KPH = 5.0
MOVE_SPEED_MPM = MOVE_SPEED_KPH * 1000 / 60
MOVE_SPEED_MPS = MOVE_SPEED_MPM / 60.0
MOVE_SPEED_PPS = MOVE_SPEED_MPS * PIXEL_PER_METER

# Pokemon Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class IDLE:
    # TODO: IDLE상태에서 움직임 구현
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dirX = 0
        self.dirY = 0
        # self.dir = self.face_dir

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        self.moving = False

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame


    @staticmethod
    def draw(self):
        if (int)(self.frame) == self.fullFrame - 1:
            self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2, (28 * 3 * 9) // 2 + 10, 28 * 3, 28 * 3)
        else:
            self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2, (28 * 3 * 9) // 2, 28 * 3, 28 * 3)

class ATTACK:
    def enter(self, event):
        print('ENTER ATTACK')
        if self.dir   == DIR_NE: self.nextX, self.nextY = 15 + 2, 9 + 2
        elif self.dir == DIR_E : self.nextX, self.nextY = 15 + 2, 9
        elif self.dir == DIR_SE: self.nextX, self.nextY = 15 + 2, 9 - 2
        elif self.dir == DIR_N : self.nextX, self.nextY = 15,     9 + 2
        elif self.dir == DIR_S : self.nextX, self.nextY = 15,     9 - 2
        elif self.dir == DIR_NW: self.nextX, self.nextY = 15 - 2, 9 + 2
        elif self.dir == DIR_W : self.nextX, self.nextY = 15 - 2, 9
        elif self.dir == DIR_SW: self.nextX, self.nextY = 15 - 2, 9 - 2
        self.u = 0.0
        self.moving = False

    def exit(self, event):
        print('EXIT ATTACK')
        useKey[RD], useKey[LD], useKey[UD], useKey[DD] = False, False, False, False
        self.moving = False

    def do(self):
        if self.moving:
            self.u -= 0.1
            if self.u < 0.0: self.add_event(STOP)
        else:
            if self.u > 1.0: self.moving = True
            else:  self.u += 0.1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame

    def draw(self):
        x = (1 - self.u) * 15 + self.u * self.nextX
        y = (1 - self.u) *  9 + self.u * self.nextY
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * x) // 2, (28 * 3 * y) // 2, 28 * 3, 28 * 3)
        pass

class MOVE:
    def enter(self, event):
        print('ENTER MOVE')
        print(f'{useKey[RD]}, {useKey[LD]}, {useKey[UD]}, {useKey[DD]}')
        print(f'enter -> {self.tempX, self.tempY}, {self.nextX, self.nextY}, {self.x, self.y}')

    def exit(self, event):
        print('EXIT MOVE')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame
        if self.moving:
            self.u += 0.05
            if self.u > 1.0:
                self.moving = False
                self.x = (int)(self.nextX)
                self.y = (int)(self.nextY)
                print(f'{self.u} aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            else:
                # TODO: 중앙에서 오른쪽 가는 골목에서 버그남
                if self.u <= 0.103:
                    # delay(0.5)
                    print(f'u<=0.103 -> {self.tempX, self.tempY}, {self.nextX, self.nextY}, {self.x, self.y}')
                else:
                    # delay(0.01)
                    pass
                self.x = (1 - self.u) * self.tempX + self.u * self.nextX
                self.y = (1 - self.u) * self.tempY + self.u * self.nextY
                print(f'aaaaaaaaaa{self.tempX, self.tempY}, {self.nextX, self.nextY}, {self.u = }')
            pass
        else:
            # TODO: 이동 후 충돌판정하기 때문에 롤백이 일어남
            if not self.moving and not useKey[RD] and not useKey[LD] and not useKey[UD] and not useKey[DD]:
                self.add_event(STOP)

            self.tempX, self.tempY = self.x, self.y
            if       useKey[RD] and not useKey[LD] and     useKey[UD] and not useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_NE, self.x + 1, self.y + 1
            elif     useKey[RD] and not useKey[LD] and not useKey[UD] and not useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_E , self.x + 1, self.y
            elif     useKey[RD] and not useKey[LD] and not useKey[UD] and     useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_SE, self.x + 1, self.y - 1
            elif not useKey[RD] and not useKey[LD] and     useKey[UD] and not useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_N , self.x,     self.y + 1
            elif not useKey[RD] and not useKey[LD] and not useKey[UD] and     useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_S , self.x,     self.y - 1
            elif not useKey[RD] and     useKey[LD] and     useKey[UD] and not useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_NW, self.x - 1, self.y + 1
            elif not useKey[RD] and     useKey[LD] and not useKey[UD] and not useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_W , self.x - 1, self.y
            elif not useKey[RD] and     useKey[LD] and not useKey[UD] and     useKey[DD]:    self.dir, self.nextX, self.nextY = DIR_SW, self.x - 1, self.y - 1
            print(f'{self.nextX, self.nextY = }, {self.x, self.y = }')

            self.moving = True
            self.u = 0.0
            print(f'{useKey[RD]}, {useKey[LD]}, {useKey[UD]}, {useKey[DD]}')
            # self.dir, self.x, self.y = DIR_NE, self.x + 1, self.y + 1
            # self.dir, self.x, self.y = DIR_E, self.x + 1, self.y
            # self.dir, self.x, self.y = DIR_SE, self.x + 1, self.y - 1
            # self.dir, self.x, self.y = DIR_N, self.x, self.y + 1
            # self.dir, self.x, self.y = DIR_S, self.x, self.y - 1
            # self.dir, self.x, self.y = DIR_NW, self.x - 1, self.y + 1
            # self.dir, self.x, self.y = DIR_W, self.x - 1, self.y
            # self.dir, self.x, self.y = DIR_SW, self.x - 1, self.y - 1

    def draw(self):
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2, (28 * 3 * 9) // 2, 28 * 3, 28 * 3)
        pass

next_state = {
    IDLE: {RU: MOVE, LU: MOVE, RD: MOVE, LD: MOVE, UD: MOVE, UU: MOVE, DD: MOVE, DU: MOVE, AD: ATTACK},
    MOVE: {RU: MOVE, LU: MOVE, RD: MOVE, LD: MOVE, UD: MOVE, UU: MOVE, DD: MOVE, DU: MOVE, STOP: IDLE},
    ATTACK: {STOP: IDLE}
}

class Pokemon:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.fullFrame = 3
        self.dir = DIR_S
        self.dirX, self.dirY = 0, 0
        self.image = None
        self.wait = 0
        self.moving = False
        self.font = load_font('ENCR10B.TTF', 16)

        # 직선 이동용 매개변수 u
        self.u = 0.0
        self.nextX, self.nextY = 0, 0
        self.tempX, self.tempY = 0, 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

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
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            if event in next_state[self.cur_state]:
                # print(f'{next_state[self.cur_state][event] = }')
                self.cur_state.exit(self, event)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw((28 * 3 * 15) // 2, (28 * 3 * 9) // 2, f'(x, y): {objects[MAINOBJECT][0].x:.2f}, {objects[MAINOBJECT][0].y:.2f})', (255, 255, 0))
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            print(f'In handle_event -> {event_name[key_event]}')
            if key_event == UD:
                useKey[UD] = True
            elif key_event == DD:
                useKey[DD] = True
            elif key_event == LD:
                useKey[LD] = True
            elif key_event == RD:
                useKey[RD] = True
            elif key_event == UU:
                useKey[UD] = False
            elif key_event == DU:
                useKey[DD] = False
            elif key_event == LU:
                useKey[LD] = False
            elif key_event == RU:
                useKey[RD] = False
            self.add_event(key_event)
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


    #     if event == UD:
    #         self.dirY += 1
    #     elif event == DD:
    #         self.dirY -= 1
    #     elif event == LD:
    #         self.dirX -= 1
    #     elif event == RD:
    #         self.dirX += 1
    #     elif event == UU:
    #         self.dirY -= 1
    #     elif event == DU:
    #         self.dirY += 1
    #     elif event == LU:
    #         self.dirX += 1
    #     elif event == RU:
    #         self.dirX -= 1


            # if self.dirX > 0 and self.dirY > 0:       self.dir, self.x, self.y = DIR_NE, self.x + 1, self.y + 1
            # elif self.dirX > 0 and self.dirY == 0:    self.dir, self.x, self.y = DIR_E , self.x + 1, self.y
            # elif self.dirX > 0 and self.dirY < 0:     self.dir, self.x, self.y = DIR_SE, self.x + 1, self.y - 1
            # elif self.dirX == 0 and self.dirY > 0:    self.dir, self.x, self.y = DIR_N , self.x, self.y + 1
            # elif self.dirX == 0 and self.dirY < 0:    self.dir, self.x, self.y = DIR_S , self.x, self.y - 1
            # elif self.dirX < 0 and self.dirY > 0:     self.dir, self.x, self.y = DIR_NW, self.x - 1, self.y + 1
            # elif self.dirX < 0 and self.dirY == 0:    self.dir, self.x, self.y = DIR_W , self.x - 1, self.y
            # elif self.dirX < 0 and self.dirY < 0:     self.dir, self.x, self.y = DIR_SW, self.x - 1, self.y - 1