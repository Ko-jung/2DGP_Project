# import Pokemon as P
from Pokemon import pokemon
from pico2d import *

class Pikachu (pokemon.Pokemon):
    def __init__(self):
        super(Pikachu, self).__init__()
        self.x, self.y = 24, 12
        self.image = load_image('Pokemon\\Image\\Pikachu.png')
        print(self.dirX, self.dirY)
        pass

    def update(self):
        super(Pikachu, self).update()
        pass

    def draw(self):
        super(Pikachu, self).draw()
        pass

    def handle_event(self, event): # 객체지향을 위해 여기서 직접 이벤트 관리, 소년이 스스로 이벤트를 처리할 수 있게
        print('pika handle_event')
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