from pico2d import *
from Pokemon.aron import Aron
from game_world import *
from Map import map
from Map import MtSteel
from Map import TinyForest
from Pokemon.pokemon import IDLE
import game_framework
import server
import pickle

import random

import square_state
import menu_state
import black_state

timage = None
pika = None
imageArray = None
backGround = None
floor = None
currFloar = None

sound = None

def enter():
    global timage
    global imageArray
    global pika
    global floor, currFloar
    global backGround, sound

    sound = load_music('Sound\\TinyForest.mp3')
    sound.set_volume(32)
    sound.repeat_play()

    server.changeState = False

    imageArray = TinyForest.TinyArray
    timage = load_image('Map\\Image\\TinyForest_Tile.png')
    floor = currFloar = 0

    randomPos = [[] for c in range(len(imageArray))]

    for n in range(len(imageArray)):
        for j in range(25):
            for i in range(48):
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
    backGround = map.Map(imageArray, timage, floor, randomPos, 'TinyForest')

    # pika = Aron(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)])
    # with open('MAINCHARDATA.pickle', 'rb') as f:
    #     pika = pickle.load(f)
    pika = server.mainChar
    pika.cur_state = IDLE
    pika.x, pika.y = randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]

    add_object(backGround, BACKOBJECT)
    add_object(pika, MAINOBJECT)

    game_framework.push_state(black_state)
    pass

def exit():
    clear()
    global timage
    global imageArray
    global pika
    global floor
    global backGround
    print(objects)

    timage = None
    imageArray = None
    pika = None
    floor = None
    backGround = None
    del backGround
    # clearBackground()
    sound.stop()
    pass

def update():
    global currFloar

    for o in all_objects():
        o.update()

    # TODO: 사망처리
    if objects[MAINOBJECT][0].isDead:
        game_framework.push_state(black_state)

    elif server.changeState:
        server.mainChar = objects[MAINOBJECT][0]
        game_framework.change_state(square_state)
    elif currFloar != objects[BACKOBJECT][0].floor:
        currFloar = objects[BACKOBJECT][0].floor
        game_framework.push_state(black_state)
    # if backGround.isOverMap(objects[MAINOBJECT][0]):
    #     objects[MAINOBJECT][0].overMap()

    pass

def draw_world():
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
        elif event.key == SDLK_i:
            game_framework.push_state(menu_state)
        elif event.key == SDLK_9:
            objects[BACKOBJECT][0].floor = 2
            objects[MAINOBJECT][0].x, objects[MAINOBJECT][0].y = 33, 20
        else:
            objects[MAINOBJECT][0].handle_event(event) # 소년한테 이벤트를 처리하도록 넘겨준다


def pause():
    pass

def resume():
    pass
