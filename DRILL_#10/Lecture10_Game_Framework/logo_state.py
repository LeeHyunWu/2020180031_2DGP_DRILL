from pico2d import *
import game_framework
import title_state
import play_state

# running = True
image = None
logo_time = 0.0

def enter(): # 객체 생성
    global image
    image = load_image('tuk_credit.png')
    # fill here
    pass

def exit(): # 객체 제거
    global image
    del image
    # fill here
    pass

def update(): # 객체 업데이트
    #logo time을 계산하고, 그 결과에 따라 1초가 넘으면 running = Flase
    global logo_time, running
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
        # running = False
    # fill here
    pass

def draw(): # 객체 그리기
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





