from pico2d import *
import math


open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')


while True:
    x = 400
    y = 90
    
    while x < 780:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 5

    while y < 550:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 5

    while x > 20:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 5

    while y > 90:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 5

    while x < 400:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 5
        
    x = 0
    y = 0
    while x < 360:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(400 + 400 * math.sin(x/360*2*math.pi), 300 - 210 * math.cos(y/360*2*math.pi))
        x = x+1
        y = y-1

