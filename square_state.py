from pico2d import *
import game_framework
import game_world
from game_world import *
import title_state
from Pokemon.aron import Aron
from rectCollision import rect

UP, DOWN, LEFT, RIGHT, S = range(5)
useKey = [False for _ in range(5)]
collision = [rect(0, 719 - 1 - 515, 362, 719 - 1 - 343)]
# 958, 719
running = True
image = None
logo_time = 0.0

mainChar = None

# Pokemon MOVE Speed
PIXEL_PER_METER = 100
MOVE_SPEED_KPH = 5.0
MOVE_SPEED_MPM = MOVE_SPEED_KPH * 1000 / 60
MOVE_SPEED_MPS = MOVE_SPEED_MPM / 60.0
MOVE_SPEED_PPS = MOVE_SPEED_MPS * PIXEL_PER_METER
RUN_SPEED_PPS = MOVE_SPEED_PPS * 2

# Pokemon Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_UP:
                useKey[UP] = True
            elif event.key == SDLK_DOWN:
                useKey[DOWN] = True
            elif event.key == SDLK_LEFT:
                useKey[LEFT] = True
            elif event.key == SDLK_RIGHT:
                useKey[RIGHT] = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                useKey[UP] = False
            elif event.key == SDLK_DOWN:
                useKey[DOWN] = False
            elif event.key == SDLK_LEFT:
                useKey[LEFT] = False
            elif event.key == SDLK_RIGHT:
                useKey[RIGHT] = False
            pass

#게임 초기화
def enter():
    print('enter square_state')
    global image
    global mainChar

    image = load_image('Map\\Image\\Square.png')
    mainChar = Aron()
    game_world.add_object(mainChar, MAINOBJECT)

    game_world.add_collision_group(mainChar, collision, 'mainChar:collision')
    pass

def update():
    if       useKey[RIGHT] and not useKey[LEFT] and     useKey[UP] and not useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_NE, +1, +1
    elif     useKey[RIGHT] and not useKey[LEFT] and not useKey[UP] and not useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_E,  +1,  0
    elif     useKey[RIGHT] and not useKey[LEFT] and not useKey[UP] and     useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_SE, +1, -1
    elif not useKey[RIGHT] and not useKey[LEFT] and     useKey[UP] and not useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_N,   0, +1
    elif not useKey[RIGHT] and not useKey[LEFT] and not useKey[UP] and     useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_S,   0, -1
    elif not useKey[RIGHT] and     useKey[LEFT] and     useKey[UP] and not useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_NW, -1, +1
    elif not useKey[RIGHT] and     useKey[LEFT] and not useKey[UP] and not useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_W,  -1,  0
    elif not useKey[RIGHT] and     useKey[LEFT] and not useKey[UP] and     useKey[DOWN]:    mainChar.dir,  mainChar.dirX,  mainChar.dirY = DIR_SW, -1, -1
    else: mainChar.dirX,  mainChar.dirY = 0, 0

    mainChar.frame = (mainChar.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
    if useKey[S] == True:
        mainChar.squareX += mainChar.dirX * RUN_SPEED_PPS * game_framework.frame_time
        mainChar.squareY += mainChar.dirY * RUN_SPEED_PPS * game_framework.frame_time
    else:
        mainChar.squareX += mainChar.dirX * MOVE_SPEED_PPS * game_framework.frame_time
        mainChar.squareY += mainChar.dirY * MOVE_SPEED_PPS * game_framework.frame_time
    # print(f'{mainChar.squareX, mainChar.squareY}')

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
        pass
    pass

def draw_world():
    global image
    #TODO: 마을 그려야함
    mainX = (int)(objects[MAINOBJECT][0].squareX)
    mainY = (int)(objects[MAINOBJECT][0].squareY)

    if 200 <= mainX <= 758 and 150 <= mainY <= 719-150:
        image.clip_draw(mainX - 200, mainY - 150, 400, (int)(400*(719/958)),
                    get_canvas_width()//2, get_canvas_width()//2, get_canvas_width(), get_canvas_width())
        image.opacify(1)
        objects[MAINOBJECT][0].draw()
    else:
        mainX = clamp(200, mainX, 758)
        mainY = clamp(150, mainY, 719-150)
        image.clip_draw(mainX - 200, mainY - 150, 400, (int)(400*(719/958)),
                    get_canvas_width()//2, get_canvas_width()//2, get_canvas_width(), get_canvas_width())
        image.opacify(0.5)
        objects[MAINOBJECT][0].square_draw()
        pass

    for c in collision:
        c.draw()

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

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




