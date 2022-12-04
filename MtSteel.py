from pico2d import *
import game_framework
from game_world import *
from Map import map
from Map import MtSteel
import server
import random
from Pokemon.pokemon import IDLE

import menu_state
import square_state
import black_state

timage1 = None
timage2 = None
pika = None
imageArray = None
backGround = None
floor = None
currFloor = None
sound = None

def enter():
    global timage1, timage2
    global imageArray
    global pika
    global floor, currFloor
    global backGround, sound

    sound = load_music('Sound\\MtSteal.mp3')
    sound.set_volume(32)
    sound.repeat_play()

    server.changeState = False

    imageArray = MtSteel.MtArray
    timage1 = load_image('Map\\Image\\MtSteel01.png')
    floor = currFloor = 5
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
        print(randomPos[n])

    timage2 = load_image('Map\\Image\\MtSteel02.png')
    backGround1 = map.Map(imageArray, timage2, floor, randomPos, 'MtSteel1')

    # pika = Aron(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)])
    pika = server.mainChar
    pika.cur_state = IDLE
    pika.x, pika.y = randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]

    # add_object(backGround2, BACKOBJECT)
    add_object(backGround1, BACKOBJECT)
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

    timage = None
    imageArray = None
    pika = None
    floor = None
    backGround = None
    # clearBackground()
    sound.stop()
    pass

def update():
    global currFloor
    for o in all_objects():
        o.update()

    if objects[MAINOBJECT][0].isDead:
        game_framework.push_state(black_state)
    elif server.changeState:
        server.mainChar = objects[MAINOBJECT][0]
        game_framework.change_state(square_state)
    elif currFloor != objects[BACKOBJECT][0].floor:
        currFloor = objects[BACKOBJECT][0].floor
        if currFloor == 4:
            timage2 = load_image('Map\\Image\\MtSteel02.png')
            objects[BACKOBJECT][0].tileImage = timage2
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
    map = objects[BACKOBJECT][0]
    print('PAUSE', map.floor)
    pass

def resume():
    map = objects[BACKOBJECT][0]
    print('resume', map.floor)
    objects[MAINOBJECT][0].moveToPos(map.startPos[map.floor][random.randint(0, len(map.startPos[map.floor]) - 1)])
    pass
