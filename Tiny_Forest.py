from pico2d import *
import game_framework
import play_state

image = None
aron = None

def enter():
    global image
    global aron
    aron = play_state.Aron(28*10, 28*10)
    image = load_image('Map\\TinyForest_1f.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    aron.update()
    delay(0.3)
    pass

def draw():
    clear_canvas()
    image.draw(1344//2, 700//2)
    aron.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                #game_framework.change_state(logo_state)





