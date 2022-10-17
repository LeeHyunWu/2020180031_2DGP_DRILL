import pico2d
import play_state
import logo_state

pico2d.open_canvas()

states = [logo_state, play_state] # list 안에 모듈을 집어 넣음
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

# start_state = logo_state #모듈을 변수로 만든다.

# start_state.enter()

# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()

# start_state = play_state
# start_state.enter()

# while start_state.running:
#     start_state.handle_events()
#     start_state.update()
#     start_state.draw()
#     pico2d.delay(0.05)
# start_state.exit()

pico2d.close_canvas()