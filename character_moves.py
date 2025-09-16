from pico2d import *

open_canvas()

character = load_image('character.png')
def move_rectangle():
    print("Hello World, This is rectangle")
    pass


def move_circle():
    print("Hello World, This is circle")
    pass


# fill here
while True:
    clear_canvas_now()
    character.draw_now(400, 90)
    move_circle()
    move_rectangle()
    delay(0.1)
    pass


close_canvas()