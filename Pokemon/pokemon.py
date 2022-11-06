from pico2d import *
from game_world import *

class Pokemon:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.fullFrame = 3
        self.dir = DIR_S
        self.dirX, self.dirY = 0, 0
        self.image = None
        self.wait = 0

    def update(self):
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

        if(self.wait % 5 == 0):
            self.frame = (self.frame + 1) % self.fullFrame
            self.wait = 0
        pass

    def draw(self):
        self.image.clip_draw(1 + 29 * self.frame, 1 + 29 * self.dir, 28, 28, (28 * 3 * 15) // 2, (28 * 3 * 9) // 2, 28 * 3, 28 * 3)
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



