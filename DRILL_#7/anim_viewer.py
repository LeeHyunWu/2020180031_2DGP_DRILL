from pico2d import *
open_canvas()

image = load_image("guri.png")


def draw_image(frame_x, frame_y):
    count = 0
    cheak = frame_x

    for count in range(count, count+2, 1):
        clear_canvas()
        image.clip_draw(frame_x * 32, frame_y * 32, 32, 32, 400, 300, 200, 200)
        update_canvas()
        delay(0.17)
        frame_x = cheak + (frame_x + 1) % 3

    for count in range(count+1, count-1, -1):
        clear_canvas()
        image.clip_draw(frame_x * 32, frame_y * 32, 32, 32, 400, 300, 200, 200)
        update_canvas()
        delay(0.17)
        frame_x = cheak + (frame_x - 1) % 3

def down_move():
    frame_x = 0
    frame_y = 7
    draw_image(frame_x, frame_y)

def up_move():
    frame_x = 0
    frame_y = 4
    draw_image(frame_x, frame_y)

def left_move():
    frame_x = 0
    frame_y = 6
    draw_image(frame_x, frame_y)

def right_move():
    frame_x = 0
    frame_y = 5
    draw_image(frame_x, frame_y)

def sleeping_1():
    frame_x = 0
    frame_y = 3
    draw_image(frame_x, frame_y)

def sleeping_2():
    frame_x = 0
    frame_y = 2
    draw_image(frame_x, frame_y)

def seat_1():
    frame_x = 0
    frame_y = 1
    draw_image(frame_x, frame_y)

def seat_2():
    frame_x = 0
    frame_y = 0
    draw_image(frame_x, frame_y)

def seat_and_look():
    frame_x = 6
    frame_y = 3
    draw_image(frame_x, frame_y)


while True:
    down_move()
    down_move()
    left_move()
    left_move()
    up_move()
    up_move()
    right_move()
    right_move()
    sleeping_1()
    sleeping_1()
    sleeping_2()
    sleeping_2()
    seat_1()
    seat_2()
    seat_2()
    seat_and_look()
    seat_and_look()

close_canvas()
