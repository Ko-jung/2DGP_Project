from pico2d import *
import game_framework
import Tiny_Forest
from Pokemon import pikachu

pika = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                game_framework.change_state(Tiny_Forest)

#게임 초기화
def enter():
    print('enter play_state')

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
