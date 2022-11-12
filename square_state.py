from pico2d import *
import game_framework
from game_world import *
import title_state

running = True
image = None
logo_time = 0.0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

#게임 초기화
def enter():
    print('enter square_state')
    global image
    image = load_image('Map\\Image\\Pokemon Square.png')
    pass

def update():
    pass

def draw_world():
    global image
    #TODO: 마을 그려야함
    drawX = (int)(objects[MAINOBJECT][0].x + printImageX + 1) - (int)(objects[MAINOBJECT][0].x - printImageX)
    drawY = (int)(objects[MAINOBJECT][0].y + printImageY + 1) - (int)(objects[MAINOBJECT][0].y - printImageY)

    image.clip_draw(0, 0, drawX * 24, drawY * 24,
                    (objects[MAINOBJECT][0].x + printImageX) * 28 * printSize + 14 * printSize,
                    (objects[MAINOBJECT][0].y + printImageY + 1) * 28 * printSize - 14 * printSize,
                    )

    # for i in range((int)(objects[MAINOBJECT][0].x - printImageX - 1), (int)(objects[MAINOBJECT][0].x + printImageX + 2)):
    #     for j in range((int)(objects[MAINOBJECT][0].y - printImageY - 1), (int)(objects[MAINOBJECT][0].y + printImageY + 2)):
    #         image.clip_draw(24 * i, 24 * j, 24, 24,
    #                          (i - objects[MAINOBJECT][0].x + printImageX) * 28 * printSize + 14 * printSize,
    #                          (j - objects[MAINOBJECT][0].y + printImageY + 1) * 28 * printSize - 14 * printSize,
    #                          28 * printSize, 28 * printSize)
    pass

# 게임월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def exit():
    pass

def pause():
    pass

def resume():
    pass





