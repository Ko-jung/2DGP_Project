from pico2d import *
import game_framework
import title_state

running = True
image = []
logo_time = 0.0

def enter():
    global image
    image.append(load_image("IntroPNG\\frame_000_delay-0.1s.png"))
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    if logo_time > 1.0:
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





