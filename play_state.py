from pico2d import *
import game_framework

class Aron:
    def __init__(self, x=None, y=None):
        self.image = load_image('Pokemon\\Aron.png')
        self.x = x
        self.y = y
        self.direct = 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame+1) % 3

    def draw(self):
        self.image.clip_draw(1 + 29 * self.frame, 1 + 29 * self.direct, 28, 28, self.x, self.y, 28*2, 28*2)

        pass

class Boy:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                #game_framework.change_state(logo_state)

#게임 초기화
def enter():
    global aron
    #global boy, grass, running
    #boys.append(Boy())
    #grass = Grass()
    #running = True

def update():
    pass

def draw_world():
    pass

# 게임월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def exit():
    pass

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()
