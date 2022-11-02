from pico2d import *
from Pokemon.pikachu import Pikachu
import game_framework
from Define import *
from Map import MtSteel
from Map import TinyForest

import random

image = None
timage = None
pika = None
imageArray = None

def enter():
    global image
    global timage
    global imageArray
    global pika

    pika = Pikachu()
    image = load_image('Map\\Image\\TinyForest_1f.png')
    timage = load_image('Map\\Image\\TinyForest_Tile.png')

    imageArray = TinyForest.TinyForest1f

    for i in range(48):
        for j in range(25):
            if imageArray[24 - j][i] == 23:
                match random.randint(0, 2):
                    case 0:
                        imageArray[24 - j][i] = 23
                        pass
                    case 1:
                        imageArray[24 - j][i] = 4
                        pass
                    case 2:
                        imageArray[24 - j][i] = 5
                        pass
            elif imageArray[24 - j][i] == 14:
                if random.randint(0, 10) <= 1:
                        imageArray[24 - j][i] = 6
            elif imageArray[24 - j][i] == 16:
                if random.randint(0, 10) <= 0:
                    imageArray[24 - j][i] = 17
    pass

def exit():
    global image
    del image
    pass

def update():
    pika.update()
    delay(0.1)
    pass

def draw():
    clear_canvas()

    for i in range(pika.x - printImageX, pika.x + printImageX + 1):
        for j in range(pika.y - printImageY, pika.y + printImageY + 1):
            if i < 48 and i >= 0 and j < 25 and j >= 0:
                timage.clip_draw(24 * (imageArray[24 - j][i] % 8), 24 * (imageArray[24 - j][i] // 8), 24, 24,
                                 (i - pika.x + printImageX) * 28 * printSize + 14 * printSize,
                                 (j - pika.y + printImageY + 1) * 28 * printSize - 14 * printSize,
                                 28 * printSize, 28 * printSize)
            else:
                timage.clip_draw(24 * (23 % 8), 24 * (23 // 8), 24, 24,
                                 (i - pika.x + printImageX) * 28 * printSize + 14 * printSize,
                                 (j - pika.y + printImageY + 1) * 28 * printSize - 14 * printSize,
                                 28 * printSize, 28 * printSize)

    # for i in range(48):
    #     for j in range(25):
    #         timage.clip_draw(24 * (imageArray[24 - j][i] % 8), 24 * (imageArray[24 - j][i] // 8), 24, 24, i * 28, j * 28, 28, 28)

    pika.draw()
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





