from pico2d import *
from Pokemon.pikachu import Pikachu
import game_framework
from game_world import *
from Map import map
from Map import MtSteel
from Map import TinyForest

import random

timage = None
pika = None
imageArray = None
backGround = None
floor = None

def enter():
    global timage
    global imageArray
    global pika
    global floor
    global backGround

    imageArray = TinyForest.TinyArray
    timage = load_image('Map\\Image\\TinyForest_Tile.png')
    floor = 0

    randomPos = [[] for c in range(len(imageArray))]

    for n in range(len(imageArray)):
        for i in range(48):
            for j in range(25):
                if imageArray[n][24 - j][i] == 23:
                    match random.randint(0, 2):
                        case 0:
                            imageArray[n][24 - j][i] = 23
                            pass
                        case 1:
                            imageArray[n][24 - j][i] = 4
                            pass
                        case 2:
                            imageArray[n][24 - j][i] = 5
                            pass
                elif imageArray[n][24 - j][i] == 14:
                    if random.randint(0, 10) <= 1:
                        imageArray[n][24 - j][i] = 6
                elif imageArray[n][24 - j][i] == 16:
                    randomPos[n].append([i, j])
                    if random.randint(0, 10) <= 0:
                        imageArray[n][24 - j][i] = 17

    backGround = map.Map(imageArray, timage, floor, randomPos)

    pika = Pikachu(randomPos[floor][random.randint(0, len(randomPos[floor]))])
    add_object(pika, MAINOBJECT)
    pass

def exit():
    clearAI()
    pass

def update():
    for o in all_objects():
           o.update()
    backGround.update()
    if backGround.isOverMap(objects[MAINOBJECT][0]):
        objects[MAINOBJECT][0].overMap()
        pass


    delay(0.1)
    pass

def draw_world():
    backGround.draw(objects[MAINOBJECT][0].x, objects[MAINOBJECT][0].y)

    # for layer in game_world.objects:
    for o in all_objects():
           o.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            print('TIny_forest handleevents')
            pika.handle_event(event) # 소년한테 이벤트를 처리하도록 넘겨준다





