from pico2d import *
import game_framework
import title_state
import play_state

# running = True
image = None

def enter(): # 객체 생성
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit(): # 객체 제거
    global image
    del image
    pass

def update(): # 객체 업데이트
    play_state.update()
    pass

def draw(): # 객체 그리기
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            # running = False
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()      # 이전 상태 push한 곳으로 복귀
                case pico2d.SDLK_j:
                    # boy가 list로 존재해야 함.
                    play_state.count += 1
                    play_state.boy = [play_state.Boy() for i in range(play_state.count)]
                    game_framework.pop_state()
                case pico2d.SDLK_k:
                    # boy가 list로 존재해야 함.
                    if(play_state.count == 1):
                        game_framework.pop_state()
                    else:
                        play_state.count -= 1
                        play_state.boy = [play_state.Boy() for i in range(play_state.count)]
                        game_framework.pop_state()


 # match-case : c언어 swith와 같은 용도로 쓰인다.

 #j, k로 소년의 수를 늘린다.
