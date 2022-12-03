from pico2d import *
import game_framework
import square_state
from game_world import *
from Map import map
from Map import MtSteel
import menu_state
import server
import random
from Pokemon.pokemon import IDLE

timage1 = None
timage2 = None
pika = None
imageArray = None
backGround = None
floor = None

def enter():
    global timage1, timage2
    global imageArray
    global pika
    global floor
    global backGround
    server.changeState = False

    imageArray = MtSteel.MtArray
    timage1 = load_image('Map\\Image\\MtSteel01.png')
    timage2 = load_image('Map\\Image\\MtSteel02.png')
    floor = 2

    print(len(imageArray))
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
    backGround = map.Map(imageArray, timage1, floor, randomPos)

    # pika = Aron(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)])
    pika = server.mainChar
    pika.cur_state = IDLE
    pika.x, pika.y = randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)]

    add_object(backGround, BACKOBJECT)
    add_object(pika, MAINOBJECT)
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
    pass

def update():
    for o in all_objects():
        o.update()
    if server.changeState:
        server.mainChar = objects[MAINOBJECT][0]
        game_framework.change_state(square_state)
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
