from pico2d import *
from game_world import *
import game_framework
from Pokemon.pokemon import Pokemon

Type_Normal, Type_Fire, Type_Water, Type_Elect, Type_Grass, Type_Ice, Type_Fight, Type_Poison, Type_Ground, Type_Flying, \
Type_Psy, Type_Bug, Type_Rock, Type_Ghost, Type_Dragon, Type_Dark, Type_Steel = range(17)

# 1 : 이벤트 정의
RD, LD, RU, LU, UD, UU, DD, DU, TIMER, SPACE = range(10)
event_name = ['RD', 'LD', 'RU', 'LU', 'UD', 'UU', 'DD', 'DU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,

    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_DOWN): DU,
}

# Pokemon MOVE Speed
PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KPH = 20.0
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
        self.dir = self.face_dir

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame

    @staticmethod
    def draw(self):
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2,
                             (28 * 3 * 9) // 2, 28 * 3, 28 * 3)


class ATTACK:
    def enter(self, event):
        print('ENTER MOVE')

    def exit(self, event):
        print('EXIT MOVE')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame

    def draw(self):
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2,
                             (28 * 3 * 9) // 2, 28 * 3, 28 * 3)
        pass


class MOVE:
    def enter(self, event):
        print('ENTER MOVE')

    def exit(self, event):
        print('EXIT MOVE')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.fullFrame

        if self.dirX > 0 and self.dirY > 0:
            self.dir, self.x, self.y = DIR_NE, self.x + 1, self.y + 1
        elif self.dirX > 0 and self.dirY == 0:
            self.dir, self.x, self.y = DIR_E, self.x + 1, self.y
        elif self.dirX > 0 and self.dirY < 0:
            self.dir, self.x, self.y = DIR_SE, self.x + 1, self.y - 1
        elif self.dirX == 0 and self.dirY > 0:
            self.dir, self.x, self.y = DIR_N, self.x, self.y + 1
        elif self.dirX == 0 and self.dirY < 0:
            self.dir, self.x, self.y = DIR_S, self.x, self.y - 1
        elif self.dirX < 0 and self.dirY > 0:
            self.dir, self.x, self.y = DIR_NW, self.x - 1, self.y + 1
        elif self.dirX < 0 and self.dirY == 0:
            self.dir, self.x, self.y = DIR_W, self.x - 1, self.y
        elif self.dirX < 0 and self.dirY < 0:
            self.dir, self.x, self.y = DIR_SW, self.x - 1, self.y - 1

    def draw(self):
        self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2,
                             (28 * 3 * 9) // 2, 28 * 3, 28 * 3)
        pass


next_state = {
    IDLE: {RU: MOVE, LU: MOVE, RD: MOVE, LD: MOVE, SPACE: IDLE},
    MOVE: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE, SPACE: MOVE},
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

        self.Level = None
        self.Exp = 0
        self.Type = None

        self.Hp = None
        self.Atk = None
        self.Def = None
        self.Sp_A = None
        self.Sp_D = None
        self.Spd = None

        self.IV_Hp = None
        self.IV_Atk = None
        self.IV_Def = None
        self.IV_Sp_A = None
        self.IV_Sp_D = None
        self.IV_Spd = None

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
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
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

    def overMap(self, x=0, y=0):
        if self.dir == DIR_NE:
            self.x += -1
            self.y += -1
        elif self.dir == DIR_E:
            self.x += -1
            self.y += 0
        elif self.dir == DIR_SE:
            self.x += -1
            self.y += 1
        elif self.dir == DIR_N:
            self.x += 0
            self.y += -1
        elif self.dir == DIR_S:
            self.x += 0
            self.y += 1
        elif self.dir == DIR_NW:
            self.x += 1
            self.y += -1
        elif self.dir == DIR_W:
            self.x += 1
            self.y += 0
        elif self.dir == DIR_SW:
            self.x += 1
            self.y += 1



