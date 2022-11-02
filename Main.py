import game_framework
from pico2d import *
from Define import *
import Tiny_Forest


if __name__ == '__main__':
    open_canvas(28 * printSize * (printImageX * 2 + 1), 28 * printSize * (printImageY * 2 + 1))
    game_framework.run(Tiny_Forest)
    close_canvas()
