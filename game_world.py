from Map.MtSteel import *
from Map.TinyForest import *
from enum import *

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

TinyForestArr = [TinyForest1f, TinyForest2f, TinyForest3f]
MtSteelArr = [MtSteel1f, MtSteel2f, MtSteel3f, MtSteel4f, MtSteel5f, MtSteel6f, MtSteel7f, MtSteel8f, MtSteel9f]

# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[],[]]

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
        del o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()