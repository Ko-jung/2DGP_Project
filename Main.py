import game_framework
from pico2d import *
import Tiny_Forest
#import play_state

if __name__ == '__main__':
    open_canvas(28*20, 28*20)
    game_framework.run(Tiny_Forest)
    close_canvas()
