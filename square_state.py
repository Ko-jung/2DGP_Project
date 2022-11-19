from pico2d import *
import game_framework
import game_world
from game_world import *
import title_state
from Pokemon.aron import Aron
from rectCollision import rect

UP, DOWN, LEFT, RIGHT, S = range(5)
useKey = [False for _ in range(5)]
collision = [rect(0, 719 - 1 - 515, 367, 719 - 1 - 343), rect( 424, 719 - 1 - 479, 439, 719 - 1 - 345), rect( 464, 719 - 1 - 471, 495, 719 - 1 - 400),
             rect( 454, 719 - 1 - 463, 505, 719 - 1 - 412), rect( 439, 719 - 1 - 446, 513, 719 - 1 - 421), rect( 423, 0, 511, 719 - 1 - 521),
             rect( 510, 719 - 1 - 605, 552, 719 - 1 - 578), rect( 0, 0, 426, 719 - 1 - 546), rect( 0, 719 - 1 - 545, 302, 719 - 1 - 515),
             rect( 0, 719 - 1 - 303, 279, 719 - 1), rect(0, 719 - 1 - 149, 958, 719-1), rect( 366, 719 - 1 - 472, 391, 719 - 1 - 345),
             rect( 320, 719 - 1 - 303, 439, 719 - 1), rect( 264, 719 - 1 - 267, 335, 719 - 1 - 248), rect( 426, 719 - 1 - 253, 470, 719 - 1),
             rect(545, 719 - 1 - 213, 958, 719 - 1),  rect( 576, 719 - 1 - 263, 958, 719 - 1),  rect( 592, 719 - 1 - 280, 958, 719 - 1),
             rect( 600, 719 - 1 - 287, 958, 719 - 1), rect( 632, 719 - 1 - 291, 687, 719 - 1 - 272), rect( 752, 719 - 1 - 291, 807, 719 - 1 - 272),
             rect( 729, 0, 958, 719 - 1 - 345), rect( 616, 0, 958, 719 - 1 - 537), rect( 552, 0, 583, 719 - 1 - 537),
             rect( 581, 0, 619, 719 - 1 - 560), rect( 592, 719 - 1 - 360, 958, 719 - 1 - 345), rect( 608, 719 - 1 - 383, 958, 719 - 1 - 361),
             rect( 624, 719 - 1 - 507, 736, 719 - 1 - 345), rect( 608, 719 - 1 - 486, 623, 719 - 1 - 416), rect( 560, 719 - 1 - 503, 575, 719 - 1 - 401)]
# 958, 719      rect( 0, 719 - 1 - , 958, 719 - 1 - )
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
    mainChar.setCur_state('INSQUARE')

    game_world.add_object(image, BACKOBJECT)
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
    #if useKey[S] == True:
    #    mainChar.squareX += mainChar.dirX * RUN_SPEED_PPS * game_framework.frame_time
    #    mainChar.squareY += mainChar.dirY * RUN_SPEED_PPS * game_framework.frame_time
    #else:
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
    # image.clip_draw(0, 0, 958, 719,
    #                 get_canvas_width()//2+(958-1260)//2, get_canvas_height()//2+(719-756)//2)

    if 200 <= mainX <= 758 and 150 <= mainY <= 719-150:
       image.clip_draw(mainX - 150, mainY - (int)(150*(719/958)), 300, (int)(300*(719/958)),
                   get_canvas_width()//2, get_canvas_height()//2, get_canvas_width(), get_canvas_height())
       objects[MAINOBJECT][0].draw()
    else:
       mainX = clamp(200, mainX, 758)
       mainY = clamp(150, mainY, 719-150)
       image.clip_draw(mainX - 150, mainY - (int)(150*(719/958)), 300, (int)(300*(719/958)),
                   get_canvas_width()//2, get_canvas_height()//2, get_canvas_width(), get_canvas_height())
       # image.opacify(0.5)
       objects[MAINOBJECT][0].square_draw()
       pass

    # for c in collision:
    #     c.draw()
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




