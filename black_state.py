import game_world
from pico2d import *
import game_framework
import title_state
import Tiny_Forest
import MtSteel
import square_state
from Pokemon.pokeDict import *
import server

image = None
opacifyValue = None
goAndBackSwitch = None
worldWidth = None
worldHeight = None
text = None
clear = False

def enter():
    print('ENTER black_state')
    global image, opacifyValue, goAndBackSwitch, worldWidth, worldHeight, text, clear
    image = load_image('BlackPic.png')
    opacifyValue = 0.0
    goAndBackSwitch = False
    worldWidth = get_canvas_width()
    worldHeight = get_canvas_height()

    if game_world.objects[game_world.MAINOBJECT][0].isDead:
        text = ' FAIL...'
        clear = True
    elif game_world.objects[game_world.BACKOBJECT][0].floor == 8:
        text = 'CLEAR!!!'
        clear = True
    else:
        if game_world.objects[game_world.BACKOBJECT][0].mapName == 'MtSteel1' or game_world.objects[game_world.BACKOBJECT][0].mapName == 'MtSteel2':
            mapName = 'MtSteel'
        else:
            mapName = 'TinyForest'
        text = mapName + ' ' + str(game_world.objects[game_world.BACKOBJECT][0].floor + 1) + 'F'
    pass

def exit():
    print('exit black_state')
    global image
    del image
    pass

def update():
    global opacifyValue, goAndBackSwitch

    if goAndBackSwitch:
        if opacifyValue < 0.0:
            opacifyValue = 0.0
            if clear:
                game_framework.quit()
            else:
                game_framework.pop_state()
        else:
            opacifyValue -= 0.01
    else:
        if opacifyValue > 1.0:
            goAndBackSwitch = True
        else:
            opacifyValue += 0.01
    pass

def draw():
    font = load_font('Font\\tvN 즐거운이야기 Medium.ttf', 160)
    clear_canvas()
    image.opacify(1)
    image.draw(0, 0, worldWidth * 2, worldHeight * 2)
    font.draw(worldWidth//2 - (len(text) * 60)//2, worldHeight//2, f'{text}', (255, 255, 255))

    image.opacify(1 - opacifyValue)
    image.draw(0, 0, worldWidth * 2, worldHeight * 2)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        pass
    #     if event.type == SDL_QUIT:
    #         game_framework.quit()
    #     elif event.type == SDL_KEYDOWN:
    #         if event.key == SDLK_ESCAPE:
    #             game_framework.pop_state()
