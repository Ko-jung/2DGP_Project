from pico2d import *
from Pokemon.aron import Aron
import game_framework
from game_world import *
from Map import map
from Map import MtSteel
from Map import TinyForest


import random

timage = None
pika = None
textbox = None
HUD = None
imageArray = None
backGround = None
floor = None

def enter():
    global timage
    global imageArray
    global pika
    global floor
    global backGround
    global textbox
    global HUD

    imageArray = TinyForest.TinyArray
    timage = load_image('Map\\Image\\TinyForest_Tile.png')
    textbox = load_image('Hud\\TextBox.png')
    HUD = load_image('HUD\\Hudd.png')
    floor = 0

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
    backGround = map.Map(imageArray, timage, floor, randomPos)

    pika = Aron(randomPos[floor][random.randint(0, len(randomPos[floor]) - 1)])


    add_object(backGround, BACKOBJECT)
    add_object(pika, MAINOBJECT)
    pass

def exit():
    clearAI()
    pass

def update():
    for o in all_objects():
        o.update()

    # if backGround.isOverMap(objects[MAINOBJECT][0]):
    #     objects[MAINOBJECT][0].overMap()
        pass

    pass

def draw_world():
    # for layer in game_world.objects:
    for o in all_objects():
           o.draw()

def draw_HUD():
    printsize = 32
    width = get_canvas_width() / 2
    level = []
    HP = []
    MaxHp = []
    # 레벨과 체력 숫자 하나하나 쪼개기
    temp = objects[MAINOBJECT][0].Level
    while temp != 0:
        level.append(temp%10)
        temp //= 10
    if objects[MAINOBJECT][0].Hp < 0:
        print('EEEEEEEEEEEEEEEERORRRRRRRRRRRRRRRRRRRRRRRRRRRROR pokemon hp is MINUS!!!!!!!')
    else:
        temp = objects[MAINOBJECT][0].Hp
        while temp != 0:
            HP.append(temp%10)
            temp //= 10
    temp = objects[MAINOBJECT][0].MaxHp
    while temp != 0:
        MaxHp.append(temp%10)
        temp //= 10

    # 층
    HUD.clip_draw(101, 9, 8, 8, printsize, get_canvas_height() - printsize//2, printsize, printsize)
    HUD.clip_draw(8 * (floor + 1), 9, 8, 8, printsize * 2, get_canvas_height() - printsize//2, printsize, printsize)

    # 레벨
    HUD.clip_draw(110, 9, 10, 8, printsize * 5, get_canvas_height() - printsize//2, printsize, printsize)
    for i in range(len(level)):
        HUD.clip_draw(8 * (level[len(level) - 1 - i]), 9, 8, 8, printsize * (6 + i), get_canvas_height() - printsize//2, printsize, printsize)

    # 체력
    HUD.clip_draw(121, 9, 13, 8, printsize * 10.5, get_canvas_height() - printsize//2, printsize*2, printsize)
    for i in range(len(HP)):
        HUD.clip_draw(8 * (HP[len(HP) - 1 - i]), 9, 8, 8, printsize * (12 + i), get_canvas_height() - printsize//2, printsize, printsize)
    HUD.clip_draw(134, 9, 8, 8, printsize * 15, get_canvas_height() - printsize//2, printsize, printsize)
    for i in range(len(MaxHp)):
        HUD.clip_draw(8 * (MaxHp[len(MaxHp) - 1 - i]), 9, 8, 8, printsize * (16 + i), get_canvas_height() - printsize//2, printsize, printsize)

    # 체력바 빨간색 초록색 순서
    maxperhp = (objects[MAINOBJECT][0].Hp/objects[MAINOBJECT][0].MaxHp)
    HUD.clip_draw(152, 0, 30, 8, printsize * 23, get_canvas_height() - printsize//2,
                  (int)((printsize * 6)), printsize)
    HUD.clip_draw(152, 9, 30, 8, printsize * 23 - (int)((printsize * 6) * (1 - maxperhp)/2), get_canvas_height() - printsize//2,
                  (int)((printsize * 6) * maxperhp), printsize)

    # 밑 대화상자
    textbox.clip_draw(0, 0, 223, 40, width, 40 * 3, (223 - 6)*3, 40*3)
    textbox.clip_draw(0, 46, 223, 40, width, 40 * 3, (223)*3, 40*3)
    pass

def draw():
    clear_canvas()
    draw_world()
    draw_HUD()
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
            objects[MAINOBJECT][0].handle_event(event) # 소년한테 이벤트를 처리하도록 넘겨준다





