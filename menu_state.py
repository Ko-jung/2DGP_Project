from pico2d import *
import game_framework
import title_state
import Tiny_Forest

textbox = None

def enter():
    global textbox
    textbox = load_image('Hud\\TextBox.png')
    pass

def exit():
    global textbox
    del textbox
    pass

def update():
    Tiny_Forest.update()
    pass

def draw():
    clear_canvas()
    Tiny_Forest.draw_world()
    width = get_canvas_width() / 2

    textbox.clip_draw(0, 0, 223, 40, width, 40 * 3, (223 - 6) * 3, 40 * 3)
    textbox.clip_draw(0, 46, 223, 40, width, 40 * 3, (223) * 3, 40 * 3)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()