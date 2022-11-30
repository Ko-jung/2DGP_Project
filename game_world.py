from Map.MtSteel import *
from Map.TinyForest import *
from enum import *
from pico2d import *

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

class DIRCODE(Enum):
    DIR_NE = 0
    DIR_E  = 1
    DIR_SE = 2
    DIR_N  = 3
    DIR_S  = 4
    DIR_NW = 5
    DIR_W  = 6
    DIR_SW = 7
    pass

DIR_NE, DIR_E, DIR_SE, DIR_N, DIR_NW, DIR_W, DIR_SW, DIR_S = range(8)
BACKOBJECT, AIOBJECT, MAINOBJECT = range(3)


printImageX = 7
printImageY = 4
printSize = 3
HUD = None
textbox = None

TinyForestArr = [TinyForest1f, TinyForest2f, TinyForest3f]
MtSteelArr = [MtSteel1f, MtSteel2f, MtSteel3f, MtSteel4f, MtSteel5f, MtSteel6f, MtSteel7f, MtSteel8f, MtSteel9f]

# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[],[]]
collision_group = dict()

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clearAI():
    for o in objects[AIOBJECT]:
        objects[AIOBJECT].remove(o)
        del o

def clearBackground():
    for o in objects[BACKOBJECT]:
        objects[BACKOBJECT].remove(o)
        del o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()

def add_collision_group(a, b, group):
    if group not in collision_group:
        print('Add new group ', group)
        collision_group[group] = [[], []]

    if a:
        if type(a) is list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)

    if b:
        if type(b) is list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)

def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group

def remove_collision_object(o):
    for pairs in collision_group.values():      # key:value에서 value에 해당하는 것만 가져온다
        if o in pairs[0]: pairs[0].remove(o)
        elif o in pairs[1]: pairs[1].remove(o)