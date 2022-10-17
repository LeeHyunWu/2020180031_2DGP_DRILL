import random

from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_boy_state
import logo_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')

        self.item = None                      # 아이템(Big_ball, ball)
        self.ball_image = load_image('ball21x21.png')
        self.Big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)
        if self.item == 'Big_ball':
            self.Big_ball_image.draw(self.x + 10, self.y + 50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            # running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)       # push_state : 밀어내기, pop을 호출하면 이곳으로 돌아온다.
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_boy_state)
            # running = False




boy = [None] # C언어의 NULL과 같은 의미
grass = None
count = 1
# running = None

# 초기화
def enter():
    global boy, grass # running
    boy = [Boy() for i in range(count)]
    grass = Grass()
    # running = True

# 종료
def exit(): # 기존의 존재한 함수를 가린다.
    global boy, grass
    del boy
    del grass

# 월드에 존재하는 객체들을 업데이트한다.
def update():
    for i in range(count):
        boy[i].update()
    # grass는 업데이트가 필요없기에 생략

def draw():
    clear_canvas()
    draw_world()            # 마우스 우클릭 : repector
    update_canvas()


def draw_world():
    grass.draw()
    for i in range(count):
        boy[i].draw()


def pause():        # pop으로 돌아오는 경우
    pass

def resume():       # pop으로 돌아오는 경우?
    pass

