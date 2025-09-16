from pico2d import *
import math
open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def move_right():
    print('right')
    for x in range(400,780,5):
        clear_canvas()
        character.draw_now(x, 90)
        grass.draw_now(400, 30)
        delay(0.01)
    pass
def move_left():
    for x in range(780,20,-5):
        clear_canvas()
        character.draw_now(x, 90)
        grass.draw_now(400, 30)
        delay(0.01)
    pass
def move_up():
    pass
def move_down():
    pass

def move_rectangle():
    print("Hello World, This is rectangle")
    move_right() #화면 절반 이동
    move_up() #화면 전부 이동
    move_left() #화면 전부 이동
    move_down() #화면 전부 이동
    move_right() #화면 절반 이동
    pass


def move_circle():
    radius = 210
    for i in range(271, -90, -1):
        angle = math.radians(i)
        x = 400 + radius * math.cos(angle)
        y = 300 + radius * math.sin(angle)
        clear_canvas()
        character.draw_now(x, y)
        grass.draw_now(400, 30)
        delay(0.01)
    pass

# fill here
while True:
    move_circle()

    move_rectangle()
    break
    #pass


close_canvas()