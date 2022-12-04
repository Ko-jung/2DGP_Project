from Pokemon.pokemon import *
from pico2d import *
from random import *
from Pokemon.aipokemon import *

class Voltorb (AiPokemon):
    def __init__(self, XY = [24, 12], level = 5):
        super(Voltorb, self).__init__()
        self.x, self.y = XY[0], XY[1]
        self.image = load_image('Pokemon\\Image\\voltorb.png')

        self.Level = level
        # self.Exp = 0
        self.Type = [Type_Elect]

        self.BS_Hp   = 40
        self.BS_Atk  = 30
        self.BS_Def  = 50
        self.BS_Sp_A = 55
        self.BS_Sp_D = 55
        self.BS_Spd  = 100
        super(Voltorb, self).setValue()

        pass

    def update(self):
        super(Voltorb, self).update()
        pass

    def draw(self):
        super(Voltorb, self).draw()
        pass

    def handle_event(self, event): # 객체지향을 위해 여기서 직접 이벤트 관리, 소년이 스스로 이벤트를 처리할 수 있게
        print('pika handle_event')
        super(Voltorb, self).handle_event(event)
        pass