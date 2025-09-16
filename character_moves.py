#2022182036 정지민
from pico2d import *
import math
open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')
def Draw_all(x,y):
    clear_canvas()
    character.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.01)

def first_move_right():
    print('right')
    for x in range(400,780,5):
        Draw_all(x,90)
    pass
def second_move_right():
    for x in range(20,400,5):
        clear_canvas()
        Draw_all(x,90)
    pass
def move_left():
    for x in range(780,20,-5):
        Draw_all(x,560)
    pass
def move_up():
    for y in range(90, 560,+5):
        Draw_all(780,y)
    pass
def move_down():
    for y in range(560,90,-5):
        Draw_all(20,y)
    pass

def move_rectangle():
    print("Hello World, This is rectangle")
    first_move_right() #화면 절반 이동
    move_up() #화면 전부 이동
    move_left() #화면 전부 이동
    move_down() #화면 전부 이동
    second_move_right() #화면 절반 이동
    pass


def move_circle():
    radius = 210
    for i in range(271, -90, -1):
        angle = math.radians(i)
        x = 400 + radius * math.cos(angle)
        y = 300 + radius * math.sin(angle)
        Draw_all(x,y)
    pass
def two_triangle_segments():
    y = 90
    for x in range(780, 400, -5):
        Draw_all(x, y)
        y += 6.18 # x는 76번 이동하니 (580-90) / 76 = 6.18
    for x in range(400, 20, -5):
        Draw_all(x, y)
        y -= 6.18
    pass # 아이디어는 first_move_right() 후 대각선 으로2번 이동
# fill here
def move_triangle():
    first_move_right()
    two_triangle_segments()
    second_move_right()
    pass
while True:
    move_rectangle()
    move_triangle()
    move_circle()
    pass


close_canvas()