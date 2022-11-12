from pico2d import *
from game_world import *
import game_framework
from Pokemon.pokemon import Pokemon

class AiPokemon(Pokemon):
    def __init__(self):
        super(AiPokemon, self).__init__()

    def update(self):
        # TODO: 8방향 중 갈 수 있는 공간 찾고, 가만히있는 상태까지 포함해서 랜덤 이동
        pass

    def draw(self):
        # print(f'{self}, {self.x, self.y = }')
        x = (self.x - objects[MAINOBJECT][0].x)
        y = (self.y - objects[MAINOBJECT][0].y)
        if - printImageX - 1 <= x <= printImageX + 1 and - printImageY - 1 <= y <= printImageY + 1:
            # print(self)
            self.image.clip_draw(1 + 29 * (int)(self.frame), 1 + 29 * self.dir, 28, 28, (28 * 3 * (15 + x * 2)) // 2,
                                 (28 * 3 * (9 + y * 2)) // 2, 28 * 3, 28 * 3)
            pass
        self.font.draw((28 * 3 * (15 + x * 2)) // 2, (28 * 3 * (9 + y * 2)) // 2, f'(x, y): {self.x:.2f}, {self.y:.2f})', (0, 0, 0))
        pass

    def handle_event(self, event):
        pass

    def moveToPos(self, XY):
        pass

    def overMap(self, x=0, y=0):
        pass



