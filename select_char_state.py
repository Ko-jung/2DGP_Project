from pico2d import *
import game_framework
import title_state
import Tiny_Forest

from Pokemon.bulbasaur import Bulbasaur
from Pokemon.charmander import Charmander
from Pokemon.squirtle import Squirtle
from Pokemon.pikachu import Pikachu
from Pokemon.meowth import Meowth
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur
from Pokemon.bulbasaur import Bulbasaur


image = None
font = None
font50 = None
miniFont = None
mbtiArr = [0, 0, 0, 0]
mbti = ''
text = ['잘 왔다!', '여기는 포켓몬 세계로 통하는 입구다!', '그 전에 간단한 질문을 몇 개 하겠다!', '성실하게 대답해주도록!',
        '약속이 30분 전에 취소된다면 기쁜가?', '암기 과목을 외울 때 무작정 쓰면서 외우는 편인가?.', '설거지하다 접시 10개깬 영희보다 훔치다 1개깬 철수가 더 나쁜가?', '과제를 제출기한 직전에 내는 편인가?',
        '그렇군! 넌 아마도...', '!', '인거같네!', '우리 세계에선 "', '이만 포켓몬 세게로 갈 준비가 다 된거같군!', '열심히 살아보게나!!']
sideText = ['Press A', '맞다면 Y, 틀리면 N']
sideTextCount = None
textCount = None
worldWidth = None
worldHeight = None

def enter():
    global image, font, font50, miniFont, worldWidth, worldHeight, textCount, sideTextCount
    image = load_image('BlackPic.png')
    font = load_font('tvN 즐거운이야기 Medium.ttf', 80)
    font50 = load_font('tvN 즐거운이야기 Medium.ttf', 50)
    miniFont = load_font('tvN 즐거운이야기 Medium.ttf', 30)
    worldWidth, worldHeight = get_canvas_width(), get_canvas_height()
    textCount = 0
    sideTextCount = 0
    pass

def exit():
    global image, font
    del image, font
    pass

def update():
    global sideTextCount, mbti
    if textCount >= 4: sideTextCount = 1
    if textCount >= 8:
        sideTextCount = 0
        if mbti is '': setMbti()
    pass

def setMbti():
    global mbtiArr, mbti
    if mbtiArr[0] > 0: mbti += 'I'
    else: mbti += 'E'
    if mbtiArr[1] > 0: mbti += 'S'
    else: mbti += 'N'
    if mbtiArr[2] > 0: mbti += 'F'
    else: mbti += 'T'
    if mbtiArr[3] > 0: mbti += 'P'
    else: mbti += 'J'

    bit = mbtiArr[0] * 8 + mbtiArr[1] * 4 + mbtiArr[2] * 2 + mbtiArr[3] * 1

    text[11] = text[11] + mbti + '" 이라고 부르지!'

def draw():
    clear_canvas()
    image.draw(0,0, worldWidth * 2, worldHeight * 2)
    if worldWidth//2 - (len(text[textCount]) * 40)//2 < 0:
        font50.draw(worldWidth//2 - (len(text[textCount]) * 25)//2, worldHeight//2, f'{text[textCount]}', (255, 255, 255))
    else:
        font.draw(worldWidth//2 - (len(text[textCount]) * 40)//2, worldHeight//2, f'{text[textCount]}', (255, 255, 255))
    miniFont.draw(worldWidth - (len(sideText[sideTextCount]) * 30)//2, 50, f'{sideText[sideTextCount]}', (255, 255, 255))
    update_canvas()
    pass

def handle_events():
    global textCount, mbtiArr
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_a and sideTextCount == 0:
                textCount += 1
            elif event.key == SDLK_y and sideTextCount == 1:
                mbtiArr[textCount - 4] += 1
                textCount += 1
            elif event.key == SDLK_n and sideTextCount == 1:
                textCount += 1
