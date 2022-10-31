from pico2d import *
import game_framework
import play_state
from Map import TinyFores1f

image = None
timage = None
aron = None
imageArray = None
printImageX = 10
printImageY = 6

def enter():
    global image
    global timage
    global aron
    global imageArray
    aron = play_state.Aron(28*10, 28*10)
    image = load_image('Map\\TinyForest_1f.png')
    timage = load_image('Map\\TinyForest_Tile.png')
    imageArray = TinyFores1f.TinyForest_1f
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

    for i in range(25):
        for j in range(48):
            if imageArray[i][j] == 16:
                timage.clip_draw(24 * (16%8), 24 * (16//8), 24, 24, i*28*2, j*28*2, 28*2, 28*2)
            if imageArray[i][j] == 23:
                timage.clip_draw(24 * (23%8), 24 * (23//8), 24, 24, i*28*2, j*28*2, 28*2, 28*2)
            pass

    #image.draw(1344//2, 700//2)
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





