from pico2d import *
import game_framework
from game_world import *
import select_char_state

running = True
image = []
gameStart = None
logo_time = 0.0
startTime = 0
sel = None
font = None
sound = None
inputSound = None

def enter():
    global image, gameStart, font, sound, inputSound

    font = load_font('Font\\ENCR10B.TTF', 16)
    gameStart = load_image("IntroPNG\\GameStart.png")
    for i in range(1, 10):
        strr = "IntroPNG\\frame_apngframe00" + (str)(i) + ".png"
        image.append(load_image(strr))
    for i in range(10, 100):
        strr = "IntroPNG\\frame_apngframe0" + (str)(i) + ".png"
        image.append(load_image(strr))
    for i in range(100,185):
        strr = "IntroPNG\\frame_apngframe" + (str)(i) + ".png"
        image.append(load_image(strr))

    inputSound = load_wav('Sound\\InputSound.wav')
    inputSound.set_volume(32)

    sound = load_music('Sound\\Intro.mp3')
    sound.set_volume(32)
    sound.repeat_play()

def exit():
    global image, gameStart, font, logo_time, startTime
    for o in range(183):
        del o
    del gameStart
    del font
    logo_time = 0.0
    startTime = 0
    sound.stop()
    pass

def handle_events():
    global logo_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif  event.type == SDL_KEYDOWN and logo_time >= 182:
            inputSound.play(1)
            game_framework.change_state(select_char_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a and logo_time >= 2:
            logo_time = 182
    pass

def draw():
    clear_canvas()
    image[(int)(logo_time)].clip_draw(0, 0, 874, 655,
                                      (28 * printSize * (printImageX * 2 + 1)) // 2,
                                      (28 * printSize * (printImageY * 2 + 1) // 2),
                                      28 * printSize * (printImageX * 2 + 1), 28 * printSize * (printImageY * 2 + 1))
    if logo_time >= 182 and startTime > 10:
        # font.draw((28 * printSize * (printImageX * 2 + 1)) // 2 - 10, (28 * printSize * (printImageY * 2 + 1) // 2) - 200, f'EASY', (155, 155, 255))
        # font.draw((28 * printSize * (printImageX * 2 + 1)) // 2,       (28 * printSize * (printImageY * 2 + 1) // 2) - 200, f'NORMAL', (155, 155, 255))
        # font.draw((28 * printSize * (printImageX * 2 + 1)) // 2 + 10, (28 * printSize * (printImageY * 2 + 1) // 2) - 200, f'HARD', (155, 155, 255))
        gameStart.clip_draw(0, 0, 79, 14,
                            (28 * printSize * (printImageX * 2 + 1)) // 2,
                            (28 * printSize * (printImageY * 2 + 1) // 2) - 200,
                            79 * 5, 14 * 5)
    update_canvas()

def update():
    global logo_time, startTime
    if logo_time < 182:
        logo_time += 0.25
    else:
        startTime = (startTime + 1) % 20
    pass

def pause():
    pass

def resume():
    pass




